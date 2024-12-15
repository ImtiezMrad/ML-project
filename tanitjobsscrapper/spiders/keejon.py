import scrapy
import csv

class KeejobSpider(scrapy.Spider):
    name = "keejob"
    start_urls = [
        "https://www.keejob.com/offres-emploi/"
    ]

    def __init__(self):
        # Initialize CSV file and writer
        self.file = open("keejob.csv", mode="w", newline="", encoding="utf-8")
        # Base columns with explicit addition of Salary and Mobility
        self.fieldnames = [
            "Title", "Company", "Location", "Job Type", "Job Link", 
            "Référence", "Publiée le", "Type de poste", "Lieu de travail", 
            "Expérience", "Étude", "Disponibilité", "Langues", "Salary", "Mobility"
        ]
        self.csv_writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        self.csv_writer.writeheader()

    def parse(self, response):
        job_posts = response.css(".block_white_a.post")
        for post in job_posts:
            title = post.css("h6 a b::text").get()
            if not title:
                title = post.css("h6 a::text").get()
            if title:
                title = ' '.join(title.split())  # Remove extra spaces

            company = post.css("div .span12.no-margin-left a b::text").get()
            if not company:
                company = post.css("div .span12.no-margin-left a ::text").get()
            if company:
                company = ' '.join(company.split())  # Remove extra spaces

            location = post.xpath(".//i[contains(@class, 'fa-map-marker')]/following-sibling::text()").get()
            if location:
                location = ' '.join(location.split())  # Remove extra spaces

            link = post.css("h6 a::attr(href)").get()
            job_link = response.urljoin(link) if link else None

            if link:
                yield response.follow(
                    job_link,
                    callback=self.parse_details,
                    meta={
                        'title': title,
                        'company': company,
                        'location': location,
                        'job_link': job_link
                    }
                )
        next_page = response.css('li.page-item a[aria-label="Next Page"]::attr(href)').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_details(self, response):
        title = response.meta['title']
        company = response.meta['company']
        location = response.meta['location']
        job_link = response.meta['job_link']

        # Extract all meta data labels and values
        meta_divs = response.css('div.meta')
        job_details = {}
        salary = None
        mobility = None

        for meta in meta_divs:
            label = meta.css('b::text').get()
            value = meta.css('::text').getall()
            value = ' '.join([v.strip() for v in value if v.strip()])  # Remove extra spaces and join

            if label and value:
                if value.lower().startswith(label.lower()):
                    value = value[len(label):].strip()

                # Assign salary and mobility based on content
                if "DT / Mois" in value or "Salaire" in label:
                    salary = ' '.join(value.split())  # Clean spaces
                if "Locale" in value or "International" in value:
                    mobility = ' '.join(value.split())  # Clean spaces

                job_details[label.strip(':')] = ' '.join(value.split())  # Clean spaces

        # Prepare row for CSV
        row = {
            "Title": title,
            "Company": company,
            "Location": location,
            "Job Type": job_details.get("Type de poste", "Unspecified"),
            "Job Link": job_link,
            "Référence": job_details.get("Référence", ""),
            "Publiée le": job_details.get("Publiée le", ""),
            "Type de poste": job_details.get("Type de poste", ""),
            "Lieu de travail": job_details.get("Lieu de travail", ""),
            "Expérience": job_details.get("Expérience", ""),
            "Étude": job_details.get("Étude", ""),
            "Disponibilité": job_details.get("Disponibilité", ""),
            "Langues": job_details.get("Langues", ""),
            "Salary": salary or "",
            "Mobility": mobility or "",
        }

        # Write the row to the CSV
        self.csv_writer.writerow(row)

    def closed(self, reason):
        # Close the CSV file when the spider finishes
        self.file.close()
