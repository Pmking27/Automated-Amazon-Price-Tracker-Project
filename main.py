import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "ENTER HERE YOUR EMAIL"
MY_PASSWORD = "ENTER HERE YOUR PASSWORD OR IF YOU ARE USING GMAIL ENTER HERE YOUR APP KEY"


product_url="https://www.amazon.in/Redgear-Mechanical-Keyboard-Spectrum-Control/dp/B08T28HSDN/ref=pd_rhf_ee_s_pd_sbs_rvi_sccl_1_1/258-2677873-8860314?pd_rd_w=nyJPu&content-id=amzn1.sym.dc04bec4-fa1d-4db1-84b4-6f2b15be4d08&pf_rd_p=dc04bec4-fa1d-4db1-84b4-6f2b15be4d08&pf_rd_r=AW2YPKWSQNDZD1HVE8HW&pd_rd_wg=TyPLJ&pd_rd_r=db913060-5557-4f67-8013-2fbb8e053d7e&pd_rd_i=B08T28HSDN&psc=1"
#YOU CAN CHANGE product_url 

header_param={
    "User-Agent":"en-US,en;q=0.9",
    "Accept-Language":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36"
}

response=requests.get(url=product_url,headers=header_param)
web_page=response.content

soup=BeautifulSoup(web_page,"lxml")
name_of_product=soup.find(name="span",id="productTitle").text.strip()
print(name_of_product)
price_of_product=soup.find(name="span",class_="a-price-whole").text
price_of_product=price_of_product.split(".")[0]

message=f"{name_of_product} is now {price_of_product}"

price_of_product=price_of_product.split(",")
price_of_product=f"{price_of_product[0]}{price_of_product[1]}"
int_price_of_product=int(price_of_product)

if int_price_of_product<2000:
    with smtplib.SMTP(host="smtp.gmail.com") as connection: #ENTER HERE YOUR EMAIL HOST SMTP ADDRESS
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Price Drop Alert!\n\n{message},\nlink:- {product_url}"
        )
