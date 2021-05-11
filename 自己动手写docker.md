# 自己动手写docker

[TOC]

## 安装配置

在windows下的WSL2中搭建了个go环境，在其中测试。

在union file system部分，开始转移到raspbian 4B上开发。

## namesapce隔离

### UTS namesapce

通过代码来实现uts namesapce隔离

```GO
/*
UTS Namespace主要用来隔离nodename和domainname两个系统标识。在UTS namespace里，每个namespace允许有自己的hostname。
系统API 中的clone()创建新的进程。根据填入的参数来判断哪些namesapce会被创建，而且它们的子进程也会被包含到这些namespace中。
*/
package main

import (
	"os/exec"
	"syscall"
	"os"
	"log"
)

func main(){
	cmd := exec.Command("sh") // 指定被fork出来的新仅次内的初始命令
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS, //使用CLONE_NEWUTS标识来创建一个UTC namesapce
	}
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	if err := cmd.Run(); err != nil {//go封装了对于系统clone()函数的调用，这段代码执行后会进入一个sh运行环境中
		log.Fatal(err)
	}
}
```

编译：

```BASH
go build uts_namespace.go
```

生成`uts_namespace`可执行文件。

然后运行

```bash
sudo ./uts_namespace
```

这就进入了一个新的sh。

我们检查下系统PID之间的关系：

```BASH
pstree -pl

# pstree -pl
init(1)─┬─init(97)─┬─init(98)───docker(99)─┬─{docker}(104)
        │          │                       ├─{docker}(105)
        │          │                       ├─{docker}(106)
        │          │                       ├─{docker}(107)
        │          │                       ├─{docker}(114)
        │          │                       ├─{docker}(115)
        │          │                       ├─{docker}(116)
        │          │                       ├─{docker}(117)
        │          │                       ├─{docker}(118)
        │          │                       ├─{docker}(119)
        │          │                       ├─{docker}(134)
        │          │                       ├─{docker}(136)
        │          │                       └─{docker}(285)
        │          ├─init(100)
        │          └─init(102)───docker-desktop-(103)─┬─{docker-desktop-}(108)
        │                                             ├─{docker-desktop-}(109)
        │                                             ├─{docker-desktop-}(110)
        │                                             ├─{docker-desktop-}(111)
        │                                             ├─{docker-desktop-}(112)
        │                                             ├─{docker-desktop-}(113)
        │                                             ├─{docker-desktop-}(132)
        │                                             ├─{docker-desktop-}(133)
        │                                             ├─{docker-desktop-}(135)
        │                                             └─{docker-desktop-}(137)
        ├─init(138)───init(139)───zsh(140)───sudo(614)───uts_namespace(615)─┬─sh(620)───pstree(622)
        │                                                                   ├─{uts_namespace}(616)
        │                                                                   ├─{uts_namespace}(617)
        │                                                                   ├─{uts_namespace}(618)
        │                                                                   └─{uts_namespace}(619)
        └─{init}(5)
```

可以看到当前sh的pid是620，它的父程序uts_namespace的pid是615，同时616~619这几个新的进行都是uts_namespace的子进程。

注意，当前sh所在的PID可以如下检查

```BASH
echo $$
```



我们查看下当前PID和父PID是否在同一个UTS名字空间：

```bash
# readlink /proc/620/ns/uts
uts:[4026533188]
# readlink /proc/615/ns/uts
uts:[4026532335]
```

的确不在。而616的名称空间和父进程615是一个

```bash
# readlink /proc/616/ns/uts
uts:[4026532335]
# readlink /proc/615/ns/uts
uts:[4026532335]
```

**在独立uts namespace中可以独立修改hostname**

```bash
# hostname
LAPTOP-UU8VIVF6
# hostname -b lgy
# hostname
lgy
```

另开 一个系统终端，可以发现宿主机的hostname并没有修改。



### IPC namespace

只要在创建进程时，添加CLONE_NEWIPC标识，就可以新建一个IPC namesapce

```go
/*
IPC Namespace用来隔离System V IPC和POSIX message queues。每一个IPC Namesapce都有自己的System V IPC和POSIX message queues。
*/
package main

import (
	"os/exec"
	"syscall"
	"os"
	"log"
)

func main(){
	cmd := exec.Command("sh") // 指定被fork出来的新仅次内的初始命令
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWIPC, //使用CLONE_NEWUTS标识来创建一个UTC namesapce，使用CLONE_NEWIPC表示来创建IPC namesapce
	}
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	if err := cmd.Run(); err != nil {//go封装了对于系统clone()函数的调用，这段代码执行后会进入一个sh运行环境中
		log.Fatal(err)
	}
}
```

编译运行

```bash
 go buld ipc_namespace.go
 sudo ./ipc_namespace
```

验证测试。

运行ipc_namespace后，会进入一个新的shell，我们查看其中的message queue

```BASH
# ipcs -q

------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages
```

空的。创建一个新的queue

```BASH
# ipcmk -Q
Message queue id: 0
# ipcs -q

------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages
0x249b404b 0          root       644        0            0
```

然后再开一个宿主机的shell，查看message queue情况

```BASH
# ipcs -q

------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages
```

空的，所以IPC隔离成功，宿主机看不到新创建的IPC namespace下的message queue。

### PID namespace

在fork进程时，加入CLONE_NEWPID标识即可。

```go
/*
PID namespace用来隔离进程ID。同样一个进程在不同的PID message里可以拥有不同的PID。
*/
package main

import (
	"os/exec"
	"syscall"
	"os"
	"log"
)

func main(){
	cmd := exec.Command("sh") // 指定被fork出来的新进程内的初始命令
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWIPC | syscall.CLONE_NEWPID, //使用CLONE_NEWUTS标识来创建一个UTC namesapce，使用CLONE_NEWIPC表示来创建IPC namesapce,使用CLONE_NEWPID标识来创建PID namespace
	}
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	if err := cmd.Run(); err != nil {//go封装了对于系统clone()函数的调用，这段代码执行后会进入一个sh运行环境中
		log.Fatal(err)
	}
}
```

编译运行

```bash
 go build pid_namespace.go
 sudo ./pid_namespace
```

查看真实的pid，在宿主机（实测在运行后的shell里也行）上运行

```bash
 pstree -pl
 
 ....
 ├─init(138)───init(139)───zsh(140)───sudo(882)───pid_namespace(883)─┬─sh(888)
        │                                                                   ├─{pid_namespace}(884)
        │                                                                   ├─{pid_namespace}(885)
        │                                                                   ├─{pid_namespace}(886)
        │                                                                   └─{pid_namespace}(887)
```

可以看到运行./pid_namespace后的pid是888，但是在运行生成的shell中检查当前pid（对比uts namespace的例子）

```bash
echo $$
```

结果pid为`1`。说明pid进行了映射。

### Mount space

在fork进程时，加入CLONE_NEWNS标识即可。

```go
/*
mount namespace用来隔离各个进程看到的挂载点的视图。在不同的Mount Namespace的进程中，看到的文件系统的层次是不一样的。在Mount Namespace中调用mount()和unmount()仅仅只会影响当前Namespace内的文件系统，而对全局的文件系统没有影响。

这个功能非常类似linux听的chroot()，它也是将某一个子目录变为根节点。Mount Namespace也可以实现这个功能，且更加灵活和安全。

Mount Namespace是Linux第一个实现的Namespace类型，因为命名方式和之后的Namespace不一样（当时并没有规划那么多的Namespace）。标识是CLONE_NEWNS
*/
package main

import (
	"os/exec"
	"syscall"
	"os"
	"log"
)

func main(){
	cmd := exec.Command("sh") // 指定被fork出来的新进程内的初始命令
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWIPC | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS, //使用CLONE_NEWUTS标识来创建一个UTC namesapce，使用CLONE_NEWIPC表示来创建IPC namesapce,使用CLONE_NEWPID标识来创建PID namespace
	}
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	if err := cmd.Run(); err != nil {//go封装了对于系统clone()函数的调用，这段代码执行后会进入一个sh运行环境中
		log.Fatal(err)
	}
}
```

编译运行

```GO
go build mount_namespace.go
sudo ./mount_namespace
```

直接查看/proc，/proc下面的文件都是保存在内存中的，是内核自动生成的。



### UID Namespace

fork进程时加入CLONE_NEWUSER标识即可。

```go
/*
User Namesapce主要用来隔离用户的用户组ID。一个进程的User ID和Group ID在User Namesapce内外是不同的。
*/
package main

import (
	"os/exec"
	"syscall"
	"os"
	"log"
)

func main(){
	cmd := exec.Command("sh") // 指定被fork出来的新进程内的初始命令
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWIPC | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS | syscall.CLONE_NEWUSER, //使用CLONE_NEWUTS标识来创建一个UTC namesapce，使用CLONE_NEWIPC表示来创建IPC namesapce,使用CLONE_NEWPID标识来创建PID namespace
	}
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	if err := cmd.Run(); err != nil {//go封装了对于系统clone()函数的调用，这段代码执行后会进入一个sh运行环境中
		log.Fatal(err)
	}
}
```

编译运行

```bash
go build uid_namespace.go
sudo ./uid_namespace
```

检查下id：

```bash
$ id
$ id
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
```



在宿主机上检查下user id和group id：

```bash
$ id
uid=1000(liguiying) gid=1000(liguiying) groups=1000(liguiying),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),117(netdev),1001(docker)
```

可以看出不一样。



## Cgroups

Cgroups就是control groups，是linux中用来对一组进行进行资源限制、控制和统计的系统级工具。可以控制的资源包括CPU、内存、存储、网络等。Cgroups中包含三个部分：cgroup、subsystem和hierarchy。

通过cgroup机制对进程进行分组，通过subsystem对每组进程进行资源控制，通过hierarchy将一组cgroup串成一个树状结构，在树状结构中，Cgroups（父级分组和subsystem设置）可以做到继承。

### cgroup

cgroup 对进程进行分组的机制。将进程分为cgroup后，就可以通过subsystem和hierarchy的方式，对一个cgroup下的进程进行资源控制。

一个进程可以是多个cgroup的成员，但是这些cgroup必须是在不同的hierarchy中。

### subsystem

subsystem就是一组资源控制的模块，每个subsystem都需要关联到一个cgroup上。一个subsystem智能附加到一个hierarchy上面。

通过cgroup工具（apt-get install  cgroup-tools)可以查看当前Kernel支持的subsystem：

```bash
➜  gitProject lssubsys -a
cpuset
cpu
cpuacct
blkio
memory
devices
freezer
net_cls
perf_event
net_prio
hugetlb
pids
rdma
```

### hierarchy

将一系列cgroup组织起来形成继承关系的树状组织结构。系统在创建新的hierarchy之后，会将系统中所有进程都加入这个hierarchy中的cgroup根节点。

### go语言实现

```GO
package main

import (
	"os/exec"
	"path"
	"os"
	"fmt"
	"io/ioutil"
	"syscall"
	"strconv"
)

const cgroupMemoryHierarchyMount = "/sys/fs/cgroup/memory"

func main(){
	//fmt.Println(os.Args[0] == "/proc/self/exe")
	if os.Args[0] == "/proc/self/exe" {
		fmt.Printf("current pid %d", syscall.Getpid())
		fmt.Println()
		cmd := exec.Command("sh", "-c", `stress --vm-bytes 200m --vm-keep -m 1`)
		cmd.SysProcAttr = &syscall.SysProcAttr{}
		cmd.Stdin = os.Stdin
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr

		if err := cmd.Run(); err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
	}

	cmd := exec.Command("/proc/self/exe")//再次执行本程序，所以会重新调用main函数一次，这样就会进入上面的代码段。上面的代码段会阻塞执行，出错后会退出，所以不用担心重复执行下面的代码
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWIPC | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS | syscall.CLONE_NEWUSER | syscall.CLONE_NEWNET,
	}
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	if err := cmd.Start(); err != nil {//cmd.Start 与 cmd.Wait 必须一起使用, cmd.Start 不用等命令执行完成，就结束
		fmt.Println("ERROR", err)
		os.Exit(1)
	} else {
		fmt.Println("fork进程映射在外部命名空间的PID：%v", cmd.Process.Pid)
		os.Mkdir(path.Join(cgroupMemoryHierarchyMount, "testmemorylimit_buildingdocker"), 0755)
		ioutil.WriteFile(path.Join(cgroupMemoryHierarchyMount, "testmemorylimit_buildingdocker", "task"), []byte(strconv.Itoa(cmd.Process.Pid)), 0644)
		ioutil.WriteFile(path.Join(cgroupMemoryHierarchyMount, "testmemorylimit_buildingdocker", "memory.limit_in_bytes"), []byte("100m"), 0644)
	}
	cmd.Process.Wait() //cmd.Wait 等待命令结束
}
```

编译运行

```BASH
go build cgroup_demo.go
sudo ./cgroup_demo
```

注意，上面代码中的/proc/self/exe是对本程序的软连接，exec.Command("/proc/self/exe")相当于重新执行本程序。



## Union File System

本书讲解的是AUFS（advanced Multi-Layered Unification Filesystem)，但是现在docker已经使用overlay2。在结构上已经发生变化，但是很多思想还是类似的。

docker的image和docker相关的文件系统会默认存在/var/lib/docker，其中容器的文件系统在/var/lib/docker/containers文件夹下，这个没有变。/var/lib/docker/containers/<container-id>目录中会保存container的metadata和配置文件。

image的则发生变化。

Docker使用CoW（copy on write）技术来实现image layer，这技术保证了在文件复制时，若不发生写入是，不会对文件进行真实复制。当对文件进行写入时，将文件即时拷贝然后在写入。

在镜像生成容器后，会在最上层的image layer上生成一个<layer-id>-init的层，这个是Docker为容器创建的read-only层，而同名的<layer-id>层则是为容器创建的read-write层。

但是，经过多方尝试，目前大部分的ubuntu内核不支持aufs，而且最新的docker支持的overlay2，所以决定采用overlay2进行开发。其原理和aufs极为相近。

创建image-layer1/2/3/4文件夹，并在其中各添加image-layer1/2/3/4.txt，里面的内容分别为“I am image layer 1/2/3/4”，这些将作为image layer的样例。然后创建container-layer文件夹，里面包含container-layer.txt，内容为“I am container-layer”

```bash
mkdir container-layer
 echo "I am a container layer" >> container-layer/container-layer.txt
 mkdir image-layer1
 mkdir image-layer2
 mkdir image-layer3
 mkdir image-layer4
 echo "I am image layer 1" >> image-layer1/image-layer1.txt
 echo "I am image layer 2" >> image-layer2/image-layer2.txt
 echo "I am image layer 3" >> image-layer3/image-layer3.txt
 echo "I am image layer 4" >> image-layer4/image-layer4.txt
```

然后创建worker和mnt两个目录

```bash
mkdir worker mnt
```

采用overlay的方式将image layer和container layer一起挂载到mnt上，注意，如果是在docker中运行则需要加入`--privileged`选项：

```bash
sudo mount -t overlay overlay -o lowerdir=image-layer1:image-layer2:image-layer3:image-layer4,upperdir=container-layer,workdir=worker mnt
```

这里image-layer1/2/3/4作为底层的只读的镜像层，container-layer作为上层的可读写层一起挂载到mnt文件夹。

查看mnt文件夹可以看到所有的文件：

overlay2也是写时复制策略。

## 容器的构造

### /proc文件系统

Linux下的**/proc**文件系统是由内核提供的，它并非一个真实的文件系统，**它只存在于内存中**，不占用外存空间。/proc以文件系统的形式，提供系统运行时的信息（系统内存、mount设备信息等）的访问接口，实际上，这些接口是以文件形式体现的，读取信息就是读取某个文件的内容。例如lsmod就是cat /proc/modules。

/proc下有很多数字命名的文件夹，这些事为每个进程创建的空间，数字就是它们的PID。

```BASH
 ➜  ~ ls /proc
1    147        cgroups    diskstats    iomem      kmsg         misc          sched_debug  sysvipc      vmstat
100  2078       cmdline    dma          ioports    kpagecgroup  modules       schedstat    thread-self  zoneinfo
101  98         config.gz  driver       irq        kpagecount   mounts        self         timer_list
107  99         consoles   execdomains  kallsyms   kpageflags   mtrr          softirqs     tty
108  acpi       cpuinfo    filesystems  kcore      loadavg      net           stat         uptime
145  buddyinfo  crypto     fs           key-users  locks        pagetypeinfo  swaps        version
146  bus        devices    interrupts   keys       meminfo      partitions    sys          vmallocinfo

```

假设N为PID，则：

```
/proc/N					PID为N的进程信息
/proc/N/cmdline			进程启动命令
/proc/N/cwd				链接到进程的当前工作目录
/proc/N/environ			进程环境变量列表
/proc/N/exe				链接到进程的执行命令文件
/proc/N/fd				包含进程相关的所有文件描述符
/proc/N/maps			与进程相关的内存映射信息
/proc/N/mem				指代进程持有的内存，不可读
/proc/N/root			链接到进程的根目录
/proc/N/stat			进程状态
/proc/N/statm			进程使用的内存状态
/proc/N/status			进程状态信息，比stat/statm更具可读性
/proc/self				链接到当前正在运行的进程
```

