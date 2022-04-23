# Git使用问题记录

## Git 账户的初始化

参考[菜鸟](https://www.runoob.com/git/git-remote-repo.html)

主要步骤如下：
1. 用Git生成账户的SSH：`ssh-keygen -t rsa -C "youremail@example.com"`
2. 在GitHub中配置SSH
3. 测量连接：`ssh -T git@github.com`

## GitHub 远程仓库增删查

```
# 查看仓库
$ git remote -v
origin    git@github.com:tianqixin/runoob-git-test.git (fetch)
origin    git@github.com:tianqixin/runoob-git-test.git (push)

# 添加仓库 origin2
$ git remote add origin2 git@github.com:tianqixin/runoob-git-test.git

$ git remote -v
origin    git@github.com:tianqixin/runoob-git-test.git (fetch)
origin    git@github.com:tianqixin/runoob-git-test.git (push)
origin2    git@github.com:tianqixin/runoob-git-test.git (fetch)
origin2    git@github.com:tianqixin/runoob-git-test.git (push)

# 删除仓库 origin2
$ git remote rm origin2
$ git remote -v
origin    git@github.com:tianqixin/runoob-git-test.git (fetch)
origin    git@github.com:tianqixin/runoob-git-test.git (push)
```

## GitHub 推送

```
# 提交变更信息到Git
$ git commit -m "添加到远程"
master 69e702d] 添加到远程
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 runoob-test.txt

 # 推送到 Github: 仓库是origin，分支是master
$ git push origin master   
```