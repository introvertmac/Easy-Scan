#!/usr/bin/env python2.7


import os
import requests
from bs4 import BeautifulSoup


site_name=raw_input("enter the website name without https:// or www\n")


#print the response headers
def get_headers():
  get_headers = requests.get("http://"+str(site_name))

  print '\n',("*" * 10) + "Here are the response headers" + ("*" * 10),"\n"
  for k in (get_headers.headers):
    print k, " : ", get_headers.headers[k]

  print "\n"

#Test for Clickjacking protections 

def clickjacking():
  get_headers= requests.get("http://"+str(site_name))
  print ("*" * 10) + "Testing for clickjacking" + ("*" * 10),"\n"

  try:
    print "Site's X-Frame value " + get_headers.headers['X-Frame-Options'],"\n"

  except KeyError:
    print "Website doesn't have Clickjacking protections","\n\n"


#Test for same site scripting
def same_site():
  same_site_scripting_test='localhost.'+str(site_name)
  print ("*" * 10) + "testing for same site scripting" + ("*" * 10),"\n"
  os.system('ping -c 4 ' + same_site_scripting_test)

#testing SPF and DMARC records
def spf_dmarc():
  print "\n",('*' * 10) + "Testing SPF and DMARC records" + ('*' * 10),"\n"

  os.system('dig txt ' + site_name)


  print ('*' * 10) + "DMARC records" + ('*' * 10),"\n"

  os.system('dig txt _dmarc.' + site_name)

#Testing for admin page
def admin_page():

  print ('*' * 10) + "Admin page testing" + ('*' * 10),"\n"

  admin_page = "http://"+site_name+"/admin"
  admin_request = requests.get(admin_page)

  if admin_request.status_code==200:
    print admin_request.history
    print "visit the admin page", admin_page
  else:
    print "admin page is protected"

#Testing for directory listing
def dir_listing():
  get_headers= requests.get("http://"+str(site_name))
  print "\n",('*' * 10) + "Testing for Directory listing" + ('*' * 10),"\n"

  soup = BeautifulSoup(get_headers.text, 'html.parser')
  try:
    if soup.img == None:
      print "no image"
    else:
      image_link = soup.img['src']
      print "Image is located at ", image_link
      break_path = image_link.split('/')
      break_path.pop()
      dir_link = "/".join(break_path)
      print "Path of the directory is ", dir_link,"\n"
      request_dir = requests.get(dir_link)
      if request_dir.status_code == 403:
        print "Directory is protected with 403"
      else:
        print "request history=",request_dir.history
        print "request statuscode=",request_dir.status_code
        print "visit the link", dir_link
  except:
    print "error occured"

def csp_validation():
  print ('*' * 10) + "Testing CSP validation" + ('*' * 10),"\n"
  url = 'http://' + site_name
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

  response = requests.get(url, headers=headers)
  
  google_bypass = "http://ajax.googleapis.com"
  cloudfront_bypass = "https://*.cloudfront.net"


  try:
    csp_header1 = response.headers['content-security-policy']
    processed_csp = csp_header1.split(" ")
    if (google_bypass or cloudfront_bypass) in processed_csp:
      print "CSP bypass possible"
    else:
      print "valid CSP so far.."

  except KeyError:
    pass

  try:
    csp_header2 = response.headers['Content-Security-Policy-Report-Only']
    processed_csp2 = csp_header2.split(" ")
    if (google_bypass or cloudfront_bypass) in processed_csp2:
      print "CSP bypass possible from CSP-report-only"
    else:
      print "valid CSP or CSP-report-only implemented"

  except KeyError:
    pass


#functions calls
get_headers()
clickjacking()
same_site()
spf_dmarc()
admin_page()
csp_validation()
dir_listing()




