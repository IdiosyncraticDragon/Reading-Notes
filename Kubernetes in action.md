# Kubernetes in action
> Marko Luksa

## Chapter 1 : Introduction
- We need automation, which includes automatic scheduling of those components to our servers, automatic configuration, supervision, and failure-handling. This is where Kubernetes comes in.
- Kubernets is becoming the standard way of running distributed apps both in the cloud, as well as on local on-premises infrastructure.
- Changes to one part of the application require a redeployment of the whole application, and over time the lack of hard boundaries between the parts results in the increase of complexity and consequential deterioration of the quality of the whole system because of the unconstrained growth of inter-dependencies between these parts.
- If any part of a monolithic application isn’t scalable, the whole application becomes unscalable, unless you can split up the monolith somehow.
- RESTful (REpresentational State Transfer) APIs
- AMQP (Advanced Message Queueing Protocol).
- With increasing numbers of microservices, this becomes tedious and error-prone, especially when you consider what the ops/sysadmin teams need to do when a server fails.
- Microservices also bring other problems, such as making it hard to debug and trace execution calls, because they span multiple processes and machines.
- Regardless of how many individual components you’re developing and deploying, one of the biggest problems that developers and operations teams always have to deal with is the differences in the environments they run their apps in.
- A process running in a container runs inside the host’s operating system, like all the other processes (unlike VMs, where processes run in separate operating systems). But the process in the container is still isolated from other processes. To the process itself, it looks like it’s the only one running on the machine and in its operating system.
- A container, on the other hand, is nothing more than a single isolated process running in the host OS, consuming only the resources that the app consumes and without the overhead of any additional processes.
- Why container is possible? Linux Namespaces, makes sure each process sees its own personal view of the system (files, processes, network interfaces, hostname, and so on). The second one is Linux Control Groups (cgroups), which limit the amount of resources the process can consume (CPU, memory, network bandwidth, and so on).
- all containers running on a host use the host’s Linux kernel.
- If a containerized application requires a specific kernel version, it may not work on every machine.
- It should also be clear that a containerized app built for a specific hardware architecture can only run on other machines that have the same architecture.
- The actual isolation of containers is done at the Linux kernel level using kernel features such as Linux Namespaces and cgroups. Docker only makes it easy to use those features
## Kubernetes: a glance
- The components of the Control Plane hold and control the state of the cluster, but they don’t run your applications. This is done by the (worker) nodes.
