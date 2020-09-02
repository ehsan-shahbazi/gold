from django.db import models
from django.utils import timezone
from urllib import request as py_request
import smtplib
import ssl
from .setting import Setting
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
setting = Setting()


class User(models.Model):
    name = models.CharField(max_length=100, name='name')
    phone = models.CharField(default='09125459232', name='phone', max_length=11)
    email = models.EmailField(default='not@gmail.com', name='email')
    last_mail = models.DateTimeField(name='last')

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(name='name', max_length=100, default='')
    persian_name = models.CharField(name='persian_name', max_length=100, default='سکّه')
    price = models.IntegerField(name="price", default=100)
    sell_price = models.IntegerField(name="sell_price", default=101)
    buy_price = models.IntegerField(name="buy_price", default=99)
    update = models.DateTimeField(name='update')
    pure_gold_weight = models.FloatField(name='pure_gold_weight', default=0)
    bulb = models.IntegerField(name='bulb', default=0)
    we_sell = models.BooleanField(name='show', default=True)
    hour_tendency = models.IntegerField(name='hour_tendency', default=0)
    hour_tendency_var = models.IntegerField(name='hour_tendency_var', default=0)
    day_tendency = models.IntegerField(name='day_tendency', default=0)
    day_tendency_var = models.IntegerField(name='day_tendency_var', default=0)
    week_tendency = models.IntegerField(name='week_tendency', default=0)
    week_tendency_var = models.IntegerField(name='week_tendency_var', default=0)
    month_tendency = models.IntegerField(name='month_tendency', default=0)
    month_tendency_var = models.IntegerField(name='month_tendency_var', default=0)

    def __str__(self):
        return self.name


class Signal(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    price = models.FloatField(name='price')
    sell_price = models.FloatField(name='sell_price', default=0)
    buy_price = models.FloatField(name='buy_price', default=0)
    date_time = models.DateTimeField(name='date_time', default=timezone.now)

    def __str__(self):
        return self.material.name + '   ---->   ' + str(self.date_time)


class Paired(models.Model):
    material1 = models.ForeignKey(Material, on_delete=models.CASCADE)
    name = models.CharField(name='name', max_length=100)
    price1 = models.FloatField(name='price1')
    price2 = models.FloatField(name='price2')
    date_time = models.DateTimeField(name='date_time')


class Wrapper(models.Model):
    material = models.ForeignKey(Material, name='material', on_delete=models.CASCADE)
    the_url = models.URLField(name='the_url', default='https://www.tgju.org')
    kind = models.IntegerField(name='kind', default=0)
    the_id = models.CharField(max_length=100, default='')
    is_active = models.BooleanField(name='is_active', default=True)

    def __str__(self):
        return self.the_url

    def get_information(self):
        if self.material.update + timezone.timedelta(minutes=setting.price_check_interval) < timezone.now():
            if self.kind == 0:
                url = self.the_url
                browser = webdriver.PhantomJS("/home/ehsan/Documents/work/Data_Works/Gold/venv/goldproj/bin/phantomjs")
                browser.get(url)
                html = browser.page_source
                soup = BeautifulSoup(html, 'html.parser')
                gold_body = soup.find(id='goldbody')
                texts = ['تمام سکه امامی', 'تمام بهار آزادی', 'نیم بهار آزادی', 'ربع بهار آزادی',
                         'سکه یک گرمی', 'سکه امامی (قبل 86)', 'سکه نیم (قبل 86)', 'سکه ربع (قبل 86)']
                names = ['sekke_emami', 'sekke', 'nim_sekke', 'rob_sekke', 'sekke_gerami', 'sekke_ghadim',
                         'nim_ghadim', 'rob_ghadim']
                for index, text in enumerate(texts):
                    product = gold_body.find(text=text).findNext()
                    coming_text = product.findNext().getText().replace(',', '')
                    if str(coming_text).isdecimal():
                        buy_price = int(product.findNext().getText().replace(',', ''))
                        sell_price = int(product.findNext().findNext().getText().replace(',', ''))
                        mat = Material.objects.filter(name=names[index])
                        price = sell_price
                        sig = Signal(material=mat[0], price=float(price),
                                     sell_price=float(sell_price), buy_price=float(buy_price),
                                     date_time=timezone.now())
                        sig.save()
                        mat = mat[0]
                        if float(mat.price) != float(price):
                            mat.price = int(price)
                            mat.sell_price = int(sell_price)
                            # print('buy price is:', mat.buy_price)
                            mat.buy_price = int(buy_price)
                        mat.update = timezone.now()
                        mat.save()

            elif self.kind == 1:
                url = self.the_url
                gold_mat = 'Ab_gerami18'
                print('hi')
                html = py_request.urlopen(str(url))

                soup = BeautifulSoup(html, 'html.parser')
                print('hi')
                gold_body = soup.find(id='ctl12_ctl17_ctl00_PriceList1_gvList')
                print(gold_body)
                texts = ['سکه امامی', 'سکه بهار آزادی', 'سکه نیم', 'سکه ربع',
                         'سکه یک گرمی', 'سکه امامي ( زير 86)', 'سکه نيم ( زير 86 )', 'سکه ربع ( زير 86 )',
                         '1 گرم طلا 18 عیار']
                names = ['sekke_emami', 'sekke', 'nim_sekke', 'rob_sekke', 'sekke_gerami', 'sekke_ghadim',
                         'nim_ghadim', 'rob_ghadim', 'Ab_gerami18']
                main_mat = Material.objects.filter(name=gold_mat)[0]
                for index, text in enumerate(texts):
                    print(text)
                    product = gold_body.find(text=text).findNext()
                    coming_text = product.getText().replace(',', '')
                    # print(str(coming_text), str(coming_text).isdecimal())
                    print(coming_text)
                    if str(coming_text):
                        buy_price = int(int(product.getText().replace(',', '')) / 10)
                        sell_price = int(int(product.findNext().findNext().getText().replace(',', '')) / 10)
                        mat = Material.objects.filter(name=names[index])

                        # print(sell_price, buy_price)
                        price = sell_price
                        sig = Signal(material=mat[0], price=float(price),
                                     sell_price=float(sell_price), buy_price=float(buy_price),
                                     date_time=timezone.now())
                        sig.save()
                        mat = mat[0]
                        if float(mat.price) != float(price):
                            mat.price = int(price)
                            mat.sell_price = int(sell_price)
                            # print('buy price is:', mat.buy_price)
                            mat.buy_price = int(buy_price)
                            mat.bulb = max(int(mat.sell_price + 5000 -
                                               mat.pure_gold_weight * main_mat.sell_price / main_mat.pure_gold_weight), 1000)
                        mat.update = timezone.now()
                        mat.save()

            else:
                response = requests.get(url=str(self.the_url))
                page = response.content
                soup = BeautifulSoup(page, 'html.parser')
                my_object = soup.find(self.kind, id=self.the_id)
                ans = my_object.find('span').getText()
                ans = ans.replace(',', '')
                sig = Signal(material=self.material, price=float(ans), date_time=timezone.now())

                sig.save()
                mat = self.material
                mat.price = float(ans)
                mat.update = timezone.now()
                mat.save()


class News(models.Model):
    title = models.CharField(name='title', max_length=1000, default='')
    publisher_name = models.CharField(name='publisher_name', max_length=100, default='Tasnim')
    date_time = models.DateTimeField(name='date_time')
    link = models.URLField(name='link')


class NewsWrapper(models.Model):
    the_url = models.URLField(name='the_url', default='https://www.tgju.org')
    kind = models.IntegerField(name='kind', default=0)

    def __str__(self):
        return self.the_url

    def is_important(self, text):
        important = ['آمریکا', 'تحریم', 'ترامپ', 'کرونا', 'جنگ', 'ظریف', 'روحانی', 'بورس', 'طلا', 'سکه']
        for word in important:
            if word in text:
                return True
        return False

    def get_information(self):
        if self.kind == 0:  # Tasnim news
            response = requests.get(url=str(self.the_url))
            page = response.content
            soup = BeautifulSoup(page, 'html.parser')
            my_objects = soup.findAll('article')
            for article in my_objects:
                if article.findAll('h2'):
                    text = article.findAll('h2')[0].getText()
                else:
                    continue
                link = 'https://www.tasnimnews.com' + str(str(article.findAll('a')[0])[9:37])
                if self.is_important(text):
                    older_news = News.objects.all()
                    existed = False
                    for older_new in older_news:
                        if older_new.link == link:
                            existed = True
                            break
                    if not existed:
                        news = News(title=text, publisher_name='Tasnim News', date_time=timezone.now(), link=link)
                        news.save()


class Manager:
    def __init__(self, speed):
        self.speed = speed

    def give_difference(self, mat1, mat2):
        pairs = mat1.paired_set.filter(name=mat1.name + '---' + mat2.name)
        # print('we have: ', len(pairs), ' data.')
        price1 = mat1.price
        price2 = mat2.price
        p1_on_p2 = [x.price1 / x.price2 for x in pairs]
        # hist = np.histogram(p1_on_p2, density=True)
        p1_on_p2_new = price1 / price2
        good_to_buy = 0
        good_to_sell = 0
        for old_data in p1_on_p2:
            if p1_on_p2_new < old_data:
                good_to_buy += 1
            else:
                good_to_sell += 1
        return good_to_buy / (good_to_buy + good_to_sell)

    def send_emails(self):
        users = User.objects.all()
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = setting.email  # Enter your Gmail address
        password = setting.password
        message = "Hi It's Mahakcoin\n"
        items = Material.objects.all()
        for item in items:
            if item.show:
                message = message + item.name + " selling: " + str(item.sell_price) + ' buying: ' +\
                          str(item.buy_price)
                if item.bulb > 10000:
                    message = message + '       The bulb of this item is: ' + str(item.bulb) + '\n'
        message = message + '\n\nGood luck '
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            for user in users:
                if user.last < timezone.now() + timezone.timedelta(days=-1):
                    server.sendmail(sender_email, user.email, message + user.name)
                    user.last = timezone.now()
                    user.save()


def give_distribution(mat1, mat2):
    signals_1 = mat1.signal_set.all()
    signals_2 = mat2.signal_set.all()
    pairs = []
    for signal_1 in signals_1:
        for signal_2 in signals_2:
            if (signal_1.date_time.date() == signal_2.date_time.date()) &\
                    (signal_1.date_time.hour == signal_2.date_time.hour) &\
                    (signal_1.date_time.minute == signal_2.date_time.minute):
                pairs.append(tuple([signal_1.price, signal_2.price]))
                paired = Paired(material1=mat1, name=mat1.name + '---' + mat2.name, price1=float(signal_1.price),
                                price2=float(signal_2.price), date_time=signal_1.date_time)
                paired.save()
    return pairs
