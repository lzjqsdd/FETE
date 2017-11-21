#ifndef __CONFIG_H__
#define __CONFIG_H__

#include "type.h"

#include<iostream>
#include<map>
#include<vector>
using namespace std;

class Config{
    public:
        Config();
        Config(const Config& config);
        Config& operator=(const Config& config);
        friend ostream& operator<<(ostream& os, const Config& config);

        int timestep; //example 30seconds per iteration
		bool sample; //是否采样
        string config_path;
        string pathdir;
        string nodedir;
		string data_path;
        logging::trivial::severity_level log_level;
        map<int,int> demands;
		vector<int> sample_linkids; //需要采样的link
		vector<int> sample_nodeids; //需要采样的node
		string sample_outpath; //采样输出位置
};

#endif
