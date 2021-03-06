#ifndef __MANAGER_H__
#define __MANAGER_H__

#include <iostream>
#include <vector>
#include <string>
#include <memory>

#include "../core/type.h"
#include "../core/link.h"
#include "../core/node.h"
#include "../core/config.h"
#include "../core/bfete.h"
#include "../core/tfete.h"
#include "../core/cfete.h"
#include "../core/gfete.h"
#include "../core/dbfete.h"

using namespace std;

//负责配置初始化、数据加载等工作
//单例模式
class Manager{
    public:
        static shared_ptr<Manager> getManager();
        void init(const Config& config);

        std::shared_ptr<FETEIf> getTestModel();
        std::shared_ptr<FETEIf> getCeilModel();
        std::shared_ptr<FETEIf> getGawronModel();
        std::shared_ptr<FETEIf> getFETEModel();
        std::shared_ptr<FETEIf> getDBModel();

    protected:
        Manager();
    private:
        static shared_ptr<Manager> _manager;
        Config _config;
};


#endif
