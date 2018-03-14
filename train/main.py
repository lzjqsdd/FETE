from train_model import *

if __name__ == '__main__':

    #train for each node
    train_for_node(node_id = 1949, nodetype = 0, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':3}) #period600
    train_for_node(node_id = 1951, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2073, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2075, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2066, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2068, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2062, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2017, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2562, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2621, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2584, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2581, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2571, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 2637, nodetype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2}) #period600
    train_for_node(node_id = 102636, nodetype = 2, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})

    #train for each pool2buffer
    train_for_pool2buffer(link_id = 1949, linktype = 0, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 1951, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2073, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2075, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':3})
    train_for_pool2buffer(link_id = 2066, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2068, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2062, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2017, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2562, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2621, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2584, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2581, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2571, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
    train_for_pool2buffer(link_id = 2637, linktype = 1, train_size = 1, param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':2})
