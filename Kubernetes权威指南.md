# Kubernetes权威指南

> 纪念版，2018年底10次印刷

kuerntes是需要不同node的上的Pod之间是可以通信的，在谷歌的GCE云环境上，GCE会负责打通不同主机上Pod的通信；在非GCE环境下，用户需要通过一些额外的网络配置，甚至采用一些软件来实现kubernetes对网络的要求。

### 网络模型

目前对于容器云的网络特性要求越来越高，跨主机容器间网络互通是基本要求，同时还有更高的各种网络策略支持，由此产生了各种网络模型，主流的由docker公司提出的Container Network Model（CNM）和CoreOS公司提出的Container Network Interface（CNI）模型。

CNM模型主要包括network sandbox，endpoint和network这三个之间进行实现。

network sandbox：容器内部的网络栈，包括网络接口、路由表、DNS等配置的管理。

Endpoint：用于将容器的sandbox与外部网络对接。可以使用veth对，open vSwitch的内部port等技术实现。一个endpoint只能加入一个network。

Network：可以直接互联的Endpoint的集合。可以通过linux网桥、VLAN等技术记性实现。

一个network包含多个endpoint，一个sandbox可以包含多个endpoint，一个endpoint仅能加入一个network。

CNI模型只涉及容器和网络。

容器：容器是拥有独立linux网络命名空间的环境。

网络：网络表示为可以互联的一组实体，这些实体拥有各自独立、唯一的IP地址。

对容器网络的设置和操作都通过插件进行具体实现。CNI的插件包括两种类型：CNI plugin和IPAM（IP Address Management） plugin。CNI plugin负责为容器配置网络资源，IPAM plugin负责对容器的IP地址进行分配和管理。

## docker网络相关基础

### linux 网络基础

linux的网络通过网络名字空间（network namespace）进行管理，处于同一个的网络名字空间的资源相互不可见。

想要连通处于两个网络名字空间的资源，需要使用Veth设备对，它们是虚拟的的一堆网卡，成对出现。通过生成一堆veth设备对，并将它们分别嵌入不同的网络名字空间，可以跨网络名字空间进行通信。

网桥将所有的网络设备（veth设备的一段，实际的网卡）连通子啊一起，实现他们之间的通信。类似于实际物理设备中的交换机。网桥是实现在系统内部的一个而成虚拟网络设备。

Netfilter是运行自linux内核中，负责维护内核中的各类挂接规则表，它附在在整个网络通信过程中维护几个挂载点。iptable负责将用户定义的相关规则记录并接入到挂载点，然后由netfilter挂载到整个网络信息的处理序列中去。

### docker网络实现

docker有四种网络模式：host（`-network=host`)，container（`--network=container:Name_or_ID`），none(--network=none)和bridge（`--network=bridge`）模式。

kubernetes管理模式下，docker通常只会使用bridge模式。在该模式下，docker daemon第一次启动时会创建虚拟网桥`docker0`，并给这个网桥分配一个子网。每一个docker容器都会创建一个（veth设备对）其中一段关联到网桥上，另一端映射到容器内的eth0设备，并从网桥的地址段给eth0分配一个IP地址。