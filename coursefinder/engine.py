from coursefinder.exceptions import InvalidCriteriaException
import logging
logger = logging.getLogger(__name__)


class Engine(object):

    def recommendCourses(self, industry_names, geo_names):
        logger.debug('Loading data..')
        from coursefinder.industries import industries
        from coursefinder.crosswalks import allCrosswalkTables, crosswalk_codes
        from coursefinder.occupations import topJobsForIndustries
        from coursefinder.joblist import joblist
        from coursefinder.courses import courses, courseIndexCols
        from coursefinder.providers import providers
        from coursefinder.postcode_areas import geo_names_to_postcode_areas

        codes = []
        for name in industry_names:
            for code, industry in industries[industries.name==name].iterrows():
                code = code.lstrip('')
                logger.debug('SIC: %s', code)
                logger.debug('SIC %s level: %d', code, industry.level)
                codes.append(code)

        if codes == []:
            raise InvalidCriteriaException('None of the industry names valid.')

        areas = geo_names_to_postcode_areas(geo_names)
        # add provider info columns (name, location, etc)
        courses = courses.join(providers, on='PUBUKPRN')
        if areas.any():
            courses_in_range = courses[courses.POSTCODE.str[:2].isin(areas)]
        else:
            courses_in_range = courses

        for crosswalk in allCrosswalkTables:
            codes = crosswalk_codes(codes, **crosswalk)

        sectorJobs = topJobsForIndustries(codes)

        subset = joblist[joblist.JOB.isin(sectorJobs.index)]
        # P(occupation|industry)
        subset = subset.join(sectorJobs, on='JOB')
        # P(industry|course) for given occupation
        subset = subset.assign(pind=(subset.PERC/100)*subset.poccind)
        # identify unique courses:
        subset = subset.set_index(courseIndexCols)
        # average over COMSBJ:
        comsbj_groups = subset.groupby(courseIndexCols+['JOB'])
        pind_by_job = comsbj_groups['pind'].mean()
        # sum over jobs
        pind = pind_by_job.groupby(courseIndexCols).sum()
        # add P(industry|course) to courses table and select 10 top matches
        return courses_in_range.join(pind).nlargest(10, columns='pind')
