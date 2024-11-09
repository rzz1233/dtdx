import scrapy


class GitSpider(scrapy.Spider):
    name = "git"
    # allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]

    def parse(self, response):
        token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        post_data = {
            "commit": "Sign in",
            "authenticity_token": token,
            "add_account":"",
            "login": "rzz1233",
            "password": "221266ren",
            "webauthn - conditional": "undefined",
            "javascript - support": "true",
            "webauthn - support": "supported",
            "webauthn - iuvpaa - support": "unsupported",
            "return_to": "https: // github.com / login",
        }
        print(post_data)
        yield scrapy.FormRequest(
            url="https://github.com/session",
            callback=self.after_login,
            formdata=post_data,
        )
    def after_login(self, response):
        yield scrapy.Request(
            url="https://github.com/",
            callback=self.check_login,
        )
    def check_login(self, response):
        print(response.xpath('/html/body/div[1]/div[5]/div/div/aside/div/div/loading-context/div/div[1]/div/div[1]/h2/text()').extract_first())
