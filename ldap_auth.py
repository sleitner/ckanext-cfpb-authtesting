import os
import ldap
from pprint import pprint 

#inject server and credentials through Ansible
ldap_server = os.environ['ldap_server']
ldap_user = os.environ['ldap_user']
ldap_pass = os.environ['ldap_pass']
#connect
con = ldap.initialize(ldap_server)
con.simple_bind_s(ldap_user, ldap_pass)
dump = con.search_s('OU=CFPB Domain Users,DC=cfpb,DC=dev', ldap.SCOPE_SUBTREE)
pprint(dump[2])
# to search for a specific user; "cn" is a field in the record. See below for additional searchable fields
user = con.search_s('OU=CFPB Domain Users,DC=cfpb,DC=dev', ldap.SCOPE_SUBTREE, "cn=*search_term*")
pprint(user)
