git submodule add https://github.com/ACL4SSR/ACL4SSR
git submodule add https://github.com/Loyalsoldier/clash-rules
git submodule add https://github.com/DivineEngine/Profiles
cd ./ACL4SSR
git checkout -b master remotes/origin/master
cd ../clash-rules
git checkout -b release remotes/origin/release
git checkout -b hidden remotes/origin/hidden
git checkout master
cd ../Profiles
git branch -m rm
git checkout -b master remotes/origin/master