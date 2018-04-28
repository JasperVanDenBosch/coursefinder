import argparse
import logging
logger = logging.getLogger(__name__)


class CommandlineInterface(object):

    def parseArguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('industry_codes', type=int, nargs='+',
                            help='One or more SIC codes of industry sectors.')
        parser.add_argument('--debug', action='store_const',
                            const=10, default=30,
                            help='Print debug messages.')
        args = parser.parse_args()
        logging.basicConfig(level=args.debug)
        logger.debug('Verbosity level: %d', args.debug)
        self.industry_codes = args.industry_codes

    def recommendCourses(self):
        """Print a list of courses that are a match for the given industry

        Args:
            industry (int): SIC code
        """
        logger.debug('Loading data..')
        from coursefinder.industries import industries, levels
        from coursefinder.crosswalks import allCrosswalkTables, crosswalk_codes
        from coursefinder.occupations import topJobsForIndustries
        from coursefinder.joblist import joblist

        codes = []
        for code in self.industry_codes:
            if code in industries.index:
                industry = industries.loc[code]
                name = industry[levels].dropna().values[0]
                logger.debug('SIC %d name: %s', code, name)
                logger.debug('SIC %d division: %s', code, industry['div'])
                logger.debug('SIC %d level: %s', code, industry.level)
                codes.append(code)
            else:
                logger.debug('Unknown SIC: %d', code)

        if codes == []:
            print('None of the SIC codes valid.')
            return

        for crosswalk in allCrosswalkTables:
            codes = crosswalk_codes(codes, **crosswalk)

        courseIndexCols = ['KISCOURSEID', 'KISMODE', 'UKPRN']

        sectorJobs = topJobsForIndustries(codes)
        # lose code as JOBLIST only uses names
        sectorJobs.index = sectorJobs.index.str.lstrip('0123456789 ')

        subset = joblist[joblist.JOB.isin(sectorJobs.index)]
        # P(occupation|industry)
        subset = subset.assign(poccind=sectorJobs.loc[subset.JOB].values)
        # P(industry|course) for given occupation
        subset = subset.assign(pind=(subset.PERC/100)*subset.poccind)
        # identify unique courses:
        courseIndexCols = ['KISCOURSEID', 'KISMODE', 'UKPRN']
        subset = subset.set_index(courseIndexCols)
        # average over COMSBJ:
        comsbj_groups = subset.groupby(courseIndexCols+['JOB'], as_index=False)
        pind_by_job = comsbj_groups['pind'].mean()
        # sum over jobs
        pind = pind_by_job.groupby(courseIndexCols).sum()
        # TODO get course title etc and pretty print
      
        
        # print(occupations.loc[str(isic4)].astype(int).nlargest())
        # subset.nlargest(5, 'pind')
