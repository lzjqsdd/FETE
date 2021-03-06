#ifndef __PREPROCESS_H__
#define __PREPROCESS_H__

#include "agent.h"
#include "link.h"
#include "node.h"

#include <vector>
#include <map>
#include <string>
using namespace std;

//data文件夹下的数据预处理
//Todo
//- 间隔30s统计采样
//- 统计每个路径上的每个link分别处理
//思路：
//首先初始化每个link的情况，（都包含了哪些车，具体的id）
//然后每隔一帧统计，以车辆为研究对象，（如果当前车辆变化了id，则对应的link的出现变化）
//
//
//根据里程来拆分buffer和pool

class PProcess{
	public:
		PProcess(const string& inpath,const string& pattern,const int &interval,const string& outpath,
        vector<vector<int>>& paths,
        map<int,shared_ptr<Node>>& nodes,
        map<int,shared_ptr<Link>>& links);
		void doSampleByTime(); //采样函数
		void doSampleByLink(vector<int> linkid); //按照link单独采样
		void doSampleByNode(vector<int> nodeid); //按照link单独采样
		void init(); //初始化各个link的数量
		void clean(); //清除以前的采样记录
        void clean(vector<int> link_ids, vector<int>node_ids); //清除制定的link或者node的文件
		vector<string> getFilelist(const string& dirpath,const string& pattern);
		void sampleByTime(const string& path, bool lastfile);
		void sampleByLink(const string& path,vector<int> link_ids, bool lastfile);
		void sampleByNode(const string& path,vector<int> node_ids, bool lastfile);
    private:
        void addHeader(const vector<int>& node_ids);
        void addCommonHeader(const vector<int>& node_ids);
	private:
		string inpath; //output_path
		string pattern; //查找通配置文件
		int interval; //采样间隔
		string outpath; //output_path
		vector<vector<int>> &paths;
		map<int,shared_ptr<Link>> mslink; //记录采样统计，<id,slink>
		map<int,shared_ptr<Agent>> magent; //记录每一时刻Agent的信息
        map<int,shared_ptr<Node>> &nodes; //根据node采样用到
        map<int,shared_ptr<Link>> &links; //加载的值
};


#endif
