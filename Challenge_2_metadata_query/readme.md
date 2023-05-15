
**Problem Statemet :** We need to write code that will query the meta data of an instance within AWS or Azure or GCP
and provide a json formatted output. 
The choice of language and implementation is up to you.


for Azure the metadata can fetch from azure metadata service/endpoint 

can use the below command to get json format directly from commandline , jq will parse output as json
curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq


**Solution:**
prepared a python function which will fetch the metadata from above api, the optional parameter as searchkey, 
if serchkey is all /empty it give the complete json output and if search key is present it return the value for given key.

