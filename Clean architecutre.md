# Clean Architecture



## 原文要点摘录



### chapter 16： independence

A good  architecture must support:

- The use cases and operation of the system
- The maintenance of the system
- The development of the system
- The deployment of the system

#### use cases

1. The most important thing a good architecture can do to support behavior is to clarify the expose that behavior so that the intent of the system is visible at the architectural level.

#### operation

1. architecture plays a more substantial, and less cosmetic role in supporting the operation of the system.
2. As strange  as it may seems, this decision is one of the options that a good architect leaves open. A system that is written as a monolith, and that depends on that monolithic structure, cannot easily be upgraded to multiple processes, multiple threads, or micro-services should the need arise.
3. By comparison, an architecture that maintains the proper isolation of its components, and does not assume the means of communication between those components, will be much easier to transition through the spectrum of threads, processes, and services as the operational needs of the system change over time.

#### development

Conway's law says:

> Ayn organization that designs a system will produce a design whose structure is a copy of the organization's communication structure

A system that must be developed by an organization with many teams and many concerns must have an architecture that facilitates independent actions by those teams, so that the teams do not interfere with each other during development. This is accomplished by properly partitioning the system into well-isolated, independently developable components. 

#### deployment

1. a good architecture helps the system to be immediately deployable after build.

2. a good architecture does not rely on dozens of little configuration scripts and property file tweaks.

3. a good architecture does not require manual creation of directories or files that must be arranged just so.

#### leaving options open

A good architecture makes the system easy to change, in all the ways that it must change, by leaving options open.

HARD: a good architecture balances all of the concerns: use cases, operation, development, deployment with a component structure that mutually satisfies them all. ------very hard!

#### decoupling layers---use cases

1. the architect wants the structure of the system to support all the necessary use cases, but does not know what all those use cases are.
2. however, the architect does know the basic intent of the system
3. so the architect can employ the single responsibility principle and the  common closure principle to separate those things that change for different reasons, and to collect those things that change for the same reasons -- given the context of the intent of the system
4. architect should to find what changes for different reasons. like UI.
5. business rules themselves may be closely tied to the application, or they may be more general. for example, **the validation of  input fields is a business rule that is closely tied to the application itself.(refer to 618!)** in contrast, the calculation of interest on an account and the counting of inventory are business rules that are more closely associated with the domain. these two different kinds of rules will change at different rates, for different reasons.
6. thus we find the system divided in to decoupled horizontal layers-- the ui, application-specific business rules, application-independent business rules, and the database, just to mention a few.

#### decoupling use cases

1. use cases change for different reasons.
2. use cases are very natural way to divide the system
3. each use case uses some ui, some application-specific business rules, some application-independent business rules, and some database functionality. ---vertical decoupling
4. if you decouple the elements of the system that change for different reasons, then you can continue to add new use cases without interfering with old ones.

#### decoupling mode

1. a good architecture leaves options open, the decoupling mode is one of those options.
2. the decoupling that we did for the sake of the use cases also helps with operations.
3. however, to take advantage of the operational benefit, the decoupling must have the appropriate mode.
4. for example, the separated components which do not depend on each other and communicate over a network of some kind---- such components are called "services" or "micro-services"
5. indeed, an architecture based on services is often called a service-oriented architecture (SoA).
6. the point being made there is that sometimes we have to separate our components all the way to the service level.
7. there are many ways to decouple layers and use cases: source code level, binary code (deployment) level, and execution unit (service) level
   - source level. we can control the dependencies between source code modules so that changes to one module do not force changes or recompilation of others. **people often call this a monolithic structure**.
   - deployment level. we can control the dependencies between deployable units such as jar files, DLLs, or shared libraries, so that changes to the source code in one module do not force others to be rebuilt and redeployed. the important thing here is that the decoupled components are partitioned into independently deployable units such as jar files.
   - service level. we can reduce the dependencies down to the level of data structures, and communicate solely through network packets such that every execution unit is entirely independent of source and binary changes to others.
8. what is the best model to use? indeed, as the project matures, the optimal mode may change.
9. one solution is to simply decouple at the service level by default. but this approach is expensive and encourages coarse-grained decoupling. 
   - no matter how "micro" the micro-services get, the decoupling is not likely to be fine-grained enough.
   - is is expensive, both in development time and in system resources.
10. one maybe: decoupling to the point where a service could be formed; but then to leaves the components in the same address space as long as possible. this leaves the option for service open.
11. a good architecture will allow a system to be born as a monolith, deployed in a single file, but then to grow into a set of independently deployable units, and then all the way to independent sercies and/or micro-services.
12. a good architecture protects the majority of the source code from those changes.

#### duplication

if two apparently duplicated sections of code evolve along different paths--if they change at different rates, and for different reasons --- then they are not true duplicates.

make sure the duplication is real.