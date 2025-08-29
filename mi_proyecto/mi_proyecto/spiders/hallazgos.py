import scrapy

class HallazgosSpider(scrapy.Spider):
    name = "hallazgos"
    allowed_domains = ["worldmetrics.org"]
    start_urls = ["https://worldmetrics.org/online-prostitution-statistics/"]

    def parse(self, response):
        # Ubica la sección "Key Findings"
        findings = response.xpath('//h2[contains(text(),"Key Findings")]/following-sibling::ul[1]/li//text()').getall()
        for f in findings:
            text = f.strip()
            if text:
                yield {"hallazgo": text}
