import scrapy
import csv

class TanitJobsSpider(scrapy.Spider):
    name = "emploi"
    start_urls = [
        "https://www.emploitunisie.com/recherche-jobs-tunisie/?",
    ]

    def __init__(self):
        # Open the CSV file and write the header
        self.file = open("emploi.csv", mode="w", newline="", encoding="utf-8")
        self.csv_writer = csv.DictWriter(
            self.file,
            fieldnames=[
                "Job Title",
                "Company Name",
                "Job Description",
                "Study Level",
                "Experience Level",
                "Contract Type",
                "Region",
                "Skills",
                "Posting Date",
                "Job Link",  # New column for job links
            ],
        )
        self.csv_writer.writeheader()

    def parse(self, response):
        for job in response.css("div.card-job"):
            job_title = job.css('h3 a::text').get()  # Job title
            company_name = job.css('a.card-job-company::text').get()  # Company name
            study_level = job.css('li:contains("Niveau d´études requis") strong::text').get()  # Study level
            experience_level = job.css('li:contains("Niveau d\'expérience") strong::text').get()  # Experience level
            contract_type = job.css('li:contains("Contrat proposé") strong::text').get()  # Contract type
            region = job.css('li:contains("Région de") strong::text').get()  # Region
            skills = job.css('li:contains("Compétences clés") strong::text').get()  # Skills
            posting_date = job.css('time::text').get()  # Posting date
            job_link = response.urljoin(job.css('h3 a::attr(href)').get())  # Absolute URL for job link

            # Write the data to the CSV file
            self.csv_writer.writerow({
                "Job Title": job_title,
                "Company Name": company_name,
                "Study Level": study_level,
                "Experience Level": experience_level,
                "Contract Type": contract_type,
                "Region": region,
                "Skills": skills,
                "Posting Date": posting_date,
                "Job Link": job_link,  # Add the job link to the row
            })

        # Follow the next page link
        next_page = response.css('.pager-next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def closed(self, reason):
        # Close the CSV file when the spider finishes
        self.file.close()
