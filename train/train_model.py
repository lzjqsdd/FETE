# 为不同节点训练使用的模型，参数调节等功能,区别于基本的模型训练功能
# 默认加载所有Node的数据(待优化)
import setting  as st
from xgboost_model import XGBModel
from dae import *
from gen_feature import *
import pandas as pd


def train_for_1949():
    #step1 load data
    origin_data = []
    #try loading dump data
    if(os.path.exists(st.data_pkl_filename) and not(st.override_pkl)):
        origin_data = pickle.load(open(st.data_pkl_filename,'rb'))
        print("[INFO] load data from : " , st.data_pkl_filename)
    else:
        load_origin_data(st.origin_data_path, [1949,1951,2077], origin_data)
        pickle.dump(origin_data, open(st.data_pkl_filename,'wb'))
    df_train_1949 = origin_data[0]

    #step2: gen_feature
    df_train_1949 = filter_cut(df_train_1949,2760,13500)
    df_train_1949 = reindex(df_train_1949,1949)
    df_train_1949 = group_frame(df_train_1949)

    #step3: train
    model_1949 = XGBModel(node_id=1949,train_data = df_train_1949, test_data=df_train_1949)
    param = {'max_depth':3, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':8}
    model_1949.train(model_path = st.xgboost_model_path, param = param)
    model_1949.loadModel(model_path = st.xgboost_model_path)
    model_1949.test()


def train_for_1951():
    #step1 load data
    origin_data = []
    #try loading dump data
    if(os.path.exists(st.data_pkl_filename) and not(st.override_pkl)):
        origin_data = pickle.load(open(st.data_pkl_filename,'rb'))
        print("[INFO] load data from : " , st.data_pkl_filename)
    else:
        load_origin_data(st.origin_data_path, [1949,1951,2077], origin_data)
        pickle.dump(origin_data, open(st.data_pkl_filename,'wb'))
    df_train_1951 = origin_data[1]

    #step2: gen_feature
    df_train_1951 = filter_cut(df_train_1951,2760,13500)
    df_train_1951 = reindex(df_train_1951,1951)
    df_train_1951 = group_frame(df_train_1951)

    #step3: train
    model_1951 = XGBModel(node_id=1951,train_data = df_train_1951, test_data=df_train_1951)
    param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':8}
    model_1951.train(model_path = st.xgboost_model_path, param = param)
    model_1951.loadModel(model_path = st.xgboost_model_path)
    model_1951.test()



def train_for_2077():
    #step1 load data
    origin_data = []
    #try loading dump data
    if(os.path.exists(st.data_pkl_filename) and not(st.override_pkl)):
        origin_data = pickle.load(open(st.data_pkl_filename,'rb'))
        print("load data from : " , st.data_pkl_filename)
    else:
        load_origin_data(st.origin_data_path, [1949,1951,2077], origin_data)
        pickle.dump(origin_data, open(st.data_pkl_filename,'wb'))
    df_train_2077 = origin_data[2]

    #step2: gen_feature
    df_train_2077= filter_cut(df_train_2077,2760,13500)
    df_train_2077 = reindex(df_train_2077,2077)
    df_train_2077 = group_frame(df_train_2077)

    #step3: train
    param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'multi:softmax', 'num_class':8}
    model_2077 = XGBModel(node_id=2077,train_data = df_train_2077, test_data=df_train_2077)
    model_2077.train(model_path = st.xgboost_model_path, param = param)
    model_2077.loadModel(model_path = st.xgboost_model_path)
    model_2077.test()

    pass