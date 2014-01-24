# get ip addresses - Barclamp proposal needs to be coded and not hard coded
   service_name = node[:rabbitmq][:config][:environment]
   proposal_name = service_name.split('-')
   bcproposal = "bc-rabbitmq-"+proposal_name[2]
   getrmip_db = data_bag_item('crowbar', bcproposal)
   rmcont1 = getrmip_db["deployment"]["rabbitmq"]["elements"]["rabbitmq"][0]
   rmcont2 = getrmip_db["deployment"]["rabbitmq"]["elements"]["rabbitmq"][1]
   rmcont3 = getrmip_db["deployment"]["rabbitmq"]["elements"]["rabbitmq"][2]
   cluster_nodes = Array.new
   rmcont1hostname = rmcont1.split('.')
   rmcont2hostname = rmcont2.split('.')
   rmcont3hostname = rmcont3.split('.')
   cluster_nodes << "rabbit@"+rmcont1hostname[0]
   cluster_nodes << "rabbit@"+rmcont2hostname[0]
   cluster_nodes << "rabbit@"+rmcont3hostname[0]
   node.default['rabbitmq']['cluster_disk_nodes'] = cluster_nodes
  #End of cluster cluster address config
