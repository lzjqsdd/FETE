#include <iostream>
#include <cstdio>
#include <sstream>
#include <chrono>
#include <signal.h>

#include <boost/program_options.hpp>


#include "./core/type.h"
#include "./core/agent.h"
#include "./core/link.h"
#include "./core/node.h"
#include "./core/config.h"
#include "./core/preprocess.h"
#include "./core/manager.h"

#include "./core/bfete.h"
#include "./core/cfete.h"
#include "./core/gfete.h"
#include "./core/tfete.h"

#include "./model/modelmanager.h"
#include "./model/model.h"

#include "./utils/tinyxml2.h"


using namespace std;
using namespace tinyxml2;

void TestModel(const Config& config)
{
    shared_ptr<ModelManager> modelManager = ModelManager::getModelManager();
    modelManager->init(config);

    int type = 0, id = 1949; //0 node, 1 link
    cout << "input model type [0-node/1-link] and id:" << endl;
    cin >> type >> id;

    vector<float> feature;
    int fnum;
    cout << "input feature num and feature value:" << endl;
    cin >> fnum;
    feature.resize(fnum);
    for(int i=0;i<fnum;++i) cin >> feature[i];

    if(type == 0){
        shared_ptr<Model> model = modelManager->getXGBoostModelByNode(id);
        float output;
        model->predict(feature, output);
        cout << "value is " << output << endl;
    }
    else{
        shared_ptr<Model> model = modelManager->getXGBoostModelByLink(id);
        float output;
        model->predict(feature, output);
        cout << "value is " << output << endl;
    }
}


void sample(const Config& config, bool sample_node, bool sample_link)
{
    //加载配置文件
    shared_ptr<Manager> manager = Manager::getManager();
    manager->init(config);

    //创建推演对象
    TFETE f(config); //主要处理类
	f.init();
    PProcess processor(config.data_path, config.data_prefix, config.timestep,config.sample_outpath,f.paths, f.nodes, f.links);
    if(config.cleanall)
        processor.clean();
    else
        processor.clean(config.sample_linkids, config.sample_nodeids);

    //sample by nodes
    if(sample_node){
        LOG_DEBUG("Sample Node ...");
        if(config.sample_nodeids.size() != 0)
            processor.doSampleByNode(config.sample_nodeids);
        else{
            vector<int> nodes;
            for(auto node:f.nodes) nodes.push_back(node.first);
            processor.doSampleByNode(nodes);
        }
    }

    //sample by links
    if(sample_link){
        LOG_DEBUG("Sample Link...");
        if(config.sample_linkids.size() != 0)
            processor.doSampleByLink(config.sample_linkids);
        else{
            vector<int> links;
            for(auto link:f.links) links.push_back(link.first);
            processor.doSampleByLink(links);
        }
    }

}


void simulation(const Config& config, model_type type)
{
    shared_ptr<Manager> manager = Manager::getManager();
    manager->init(config);

    //创建推演对象
	shared_ptr<FETEIf> model = shared_ptr<FETEIf>();
    
    switch(type){
        case FETE:      model = manager->getFETEModel();    break;
        case CEIL:      model = manager->getCeilModel();    break;
        case GAWRON:    model = manager->getGawronModel();  break;
        case TEST:      model = manager->getTestModel();    break;
        case DB:        model = manager->getDBModel();      break;
    }

	model->init();
    auto stime = chrono::system_clock::now();
    model->start();
    auto etime = chrono::system_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(etime-stime);

    LOG_INFO(my2string("Total Time is : ", duration.count()," ms"));
}


void stop()
{
    std::cout << "Force stop fete!" << std::endl;
    exit(-1);
}


int main(int argc, char *argv[])
{
    namespace po = boost::program_options;
    po::options_description desc("\ndbsim [options] [ceil|test|gawron|fete] ");
    desc.add_options()
        ("help,h","show help")
        ("config,c",po::value<string>() , "user defined config file")
        ("sample,s", po::value<vector<string> >() ,"sample for node and link")
        ("simulation,S", po::value< vector<string> > (),"simulation for fast ete")
        ("test,t","Test each model")
        ;

    po::positional_options_description p;
    p.add("simulation",-1); //-1表示后面可以跟的参数无限
    p.add("sample",2);
    po::variables_map vm;
    po::store(po::command_line_parser(argc,argv).options(desc).positional(p).run(), vm);
    po::notify(vm);

    string config_file = "../config/config.conf"; //default 
    if(vm.count("config")){
       config_file = vm["config"].as<string>(); 
       cout << "using " << config_file << endl;
    }
    else{
       cout << "using defalut config" << endl;
    }

    if(vm.count("help")){
        cout << desc << "\n";
        return 0;
    }

    if(vm.count("sample")){
        Config config(config_file);
        initlog(config.log_level);
        LOG_TRACE(config);
        vector<string> sample_args = vm["sample"].as< vector<string> >();
        bool sample_node = false;
        bool sample_link = false;
        for(auto sarg : sample_args)
        {
            if(sarg == "link") sample_link = true;
            else if(sarg == "node") sample_node = true;
        }
        sample(config, sample_node, sample_link);
        return 0;
    }

    if(vm.count("simulation")){
        Config config(config_file);
        initlog(config.log_level);
        cout << config << endl;
        vector<string> simu_args = vm["simulation"].as< vector<string> >();
        for(auto sarg : simu_args) simulation(config, str2type(sarg));
        return 0;
    }
    
    if(vm.count("test")){
        Config config(config_file);
        initlog(config.log_level);
        cout << config << endl;
        TestModel(config);
        return 0;
    }

    cout << desc << "\n";
    return 1;
}
