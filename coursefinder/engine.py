from coursefinder.exceptions import InvalidCriteriaException
import logging
logger = logging.getLogger(__name__)


class Engine(object):

    def recommendCourses(self, industry_codes, geo_names):
        logger.debug('Loading data..')
        from coursefinder.industries import industries, levels
        from coursefinder.crosswalks import allCrosswalkTables, crosswalk_codes
        from coursefinder.occupations import topJobsForIndustries
        from coursefinder.joblist import joblist
        from coursefinder.courses import courses, courseIndexCols
        from coursefinder.providers import providers
        from coursefinder.postcode_areas import geo_names_to_postcode_areas

        codes = []
        for code in industry_codes:
            if code in industries.index:
                industry = industries.loc[code]
                name = industry[levels].dropna().values[0]
                print('\nIndustry name: ' + name)
                logger.debug('SIC %d division: %s', code, industry['div'])
                logger.debug('SIC %d level: %s', code, industry.level)
                codes.append(code)
            else:
                logger.debug('Unknown SIC: %d', code)

        if codes == []:
            raise InvalidCriteriaException('None of the SIC codes valid.')

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
        subset = subset.assign(poccind=sectorJobs.loc[subset.JOB].values)
        # P(industry|course) for given occupation
        subset = subset.assign(pind=(subset.PERC/100)*subset.poccind)
        # identify unique courses:
        subset = subset.set_index(courseIndexCols)
        # average over COMSBJ:
        comsbj_groups = subset.groupby(courseIndexCols+['JOB'])
        pind_by_job = comsbj_groups['pind'].mean()
        # sum over jobs
        pind = pind_by_job.groupby(courseIndexCols).sum()
        # add P(industry|course) to courses table and select 5 top matches
        return courses_in_range.join(pind).nlargest(5, columns='pind')
