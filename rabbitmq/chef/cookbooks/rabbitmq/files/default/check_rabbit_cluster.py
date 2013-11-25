#!/usr/bin/python
# Keith Rochford - Dell Cloud Centre of Excellence, Dublin
# ./check_rabbit_cluster.py -h 10.125.0.11 -t 15672 -u guest -p guest -n 2
 
import getopt, sys, urllib2, simplejson 

nagios_codes = dict(OK=0, WARNING=1, CRITICAL=2, UNKNOWN=3, DEPENDENT=4)

def usage():
    nagios_return('UNKNOWN', 'usage: %s -h host -t port -u user -p password -n count\n'% (format(sys.argv[0])))

def nagios_return(code, response):
    print(code + ": " + response)
    sys.exit(nagios_codes[code])
    
def check_node_count(host, port, user, password, benchmark):
	# create a password manager
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	
	# Add the username and password.
	# If we knew the realm, we could use it instead of None.
	top_level_url = 'http://'+host+':'+port
	password_mgr.add_password(None, top_level_url, user, password)
	
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	
	# create "opener" (OpenerDirector instance)
	opener = urllib2.build_opener(handler)
	
	# use the opener to fetch a URL
	try:
	    response = opener.open(top_level_url+'/api/nodes')
	    
	except urllib2.URLError as e:
		if hasattr(e, 'reason'):
			return {'code':'UNKNOWN', 'msg': "UKNOWN - Connection Failed: - "+ str(e.reason)}
		elif hasattr(e, 'code'):
			return {'code':'UNKNOWN', 'msg': "UKNOWN - Server Error: - "+ str(e.code)}
	else:
		json_object = simplejson.load(response)
		cluster_size = len(json_object)
		if int(cluster_size) >= int(benchmark):
			return {'code':'OK', 'msg': 'Cluster Node count: '+str(cluster_size)}
		else:
			return {'code':'WARNING', 'msg': 'Cluster Node count: '+str(cluster_size)+'. Expected value: '+str(benchmark)}
	
def main():
	if len(sys.argv) < 11: usage()
	
	#set default values
	#host = '127.0.0.1'
	#port = 15672
	#user = 'guest'
	#password = 'guest'
	#benchmark = 1

	try: opts, args = getopt.getopt(sys.argv[1:], 'h:t:u:p:n:')
	except getopt.GetoptError as err: usage()

	host = test = None

	for o, value in opts:
		#print value
		if o == "-h": host = value
		elif o == "-t": port = value
		elif o == "-u": user = value
		elif o == "-p": password = value
		elif o == "-n": benchmark = value
		else: print usage()
	
	result = check_node_count(host, port, user, password, benchmark)
	nagios_return(result['code'], result['msg'])

if __name__ == "__main__":
    main()	
