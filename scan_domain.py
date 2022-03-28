import os
import argparse


def scan_domain(domain):
	#amass_domain = os.system('./amass enum --passive -d %s -o domains_%s'%(domain,domain))
	#assetfinder_domain = os.system('./assetfinder --subs-only %s |tee -a domains_%s'%(domain,domain))
	subfinder_domain = os.system('./scan_domain/subfinder -d %s -o output/domains_subfinder_%s'%(domain,domain))
	#sub_merge = os.system('cat domains_subfinder_%s | tee -a domain_%s'%(domain,domain))
	#sort_domain = os.system('sort -u domains_%s -o domains_%s'%(domain,domain))
	#filter_domain = os.system('cat domains_%s |./filter-resolved | tee -a domains_%s.txt'%(domain,domain))
	result_domain = os.popen('cat output/domains_subfinder_%s'%domain)
	res = result_domain.read()
	for line in res.splitlines():
		return(line)

#domain = 'douyu.com'
#scan_domain(domain)

def check_domain(domain_file,domain):
	port = """80-85,8000-8010,8070-8090,443,9098,3128,1080,10880,9090,9091,9200,9443,9988,9981,10000"""
	os.system('cat %s | ./httpx -mc 200,302,301,404 -t 200 -p %s -o output/survival_%s.txt'%(domain_file,port,domain))


def dirb_domain(check_list_file,domain):
	dirb_url = os.system("python3 dirsearch/dirsearch.py -l %s --include-status=200 --plain-text-report=output/dirb_%s.txt"%(check_list_file,domain))


def sort_url(dirb_output,domain):
	result_domain = os.system('cat %s|grep 200|sort -u|awk \'{print $3}\' > output/sort_%s.txt'%(dirb_output,domain))
	print(('cat %s|grep 200|sort -u|awk \"{print $3}\" > output/sort_%s.txt'%(dirb_output,domain)))
	#res = result_domain.read()
	#for line in res.splitlines():
	#	return(line)



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Check the balance')
	parser.add_argument('--url', '-u', help='Enter the url',required=True)
	args = parser.parse_args()
	#open_file("/Users/markjayden/Mydisk/Tools/Information/JSFinder/gf1.txt")
	domain = args.url
	scan_domain(domain)
	domain_file = "output/domains_subfinder_%s"%domain
	check_domain(domain_file,domain)
	check_list = "output/survival_%s.txt"%domain
	print(check_list)
	dirb_domain(check_list,domain)
	dirb_output = "output/dirb_%s.txt"%domain
	sort_url(dirb_output,domain)

