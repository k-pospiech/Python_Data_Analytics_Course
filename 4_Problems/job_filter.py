# cell magic command to write the contents of this cell to a file called job_filter.py

def filter_by_location(list_of_job_postings, location):
    filter_postings = lambda posting: location in posting['location']
    qualified = list(filter(filter_postings, list_of_job_postings))
    qualified_titles = [job['title'] for job in qualified]
    return qualified_titles
