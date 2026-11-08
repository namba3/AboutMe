# ABOUT ME

## SUMMARY

As a software engineer, I have worked across a range of domains, primarily web services, as well as industrial IoT, machine-tool data collection and remote monitoring, and 3D model viewers. My experience includes web applications built with C#, TypeScript, and JavaScript, along with API servers and data integration systems using Rust and Go.

I emphasize performance, safety, maintainability, and ease of change in software design and implementation. My work has ranged from incremental improvements to existing systems to major application renewals, including separation of responsibilities, management of dependencies, and API boundary design. I also collaborate with product planners, designers, and developers in other departments to refine requirements and improve product quality from an engineering perspective.

In personal projects, I primarily use Rust to explore systems programming and software architecture. Beyond implementation, I am interested in the design principles and technical trade-offs behind software, and I continue to learn and experiment with new approaches.

## EDUCATION AND EMPLOYMENT

- Current employer: Kakaku.com, Inc. (Software Engineer)
- Previous employer: Core Concept Technologies Inc. (Software Engineer)
- Highest degree: Master's degree in Computer Science

| Date (newest first) | Employment | Education |
| --- | --- | --- |
| November 2022 | Joined Kakaku.com, Inc. | |
| November 2021 | Left Core Concept Technologies Inc. | |
| April 2018 | Joined Core Concept Technologies Inc. | |
| March 2018 | Left Hammock Corporation | Completed the master's program at the Graduate School of Informatics and Engineering, The University of Electro-Communications |
| September 2017 | Completed internship at Fixstars Corporation | |
| August 2017 | Started internship at Fixstars Corporation | |
| April 2016 | | Entered the master's program at the Graduate School of Informatics and Engineering, The University of Electro-Communications |
| March 2016 | | Graduated from the Faculty of Informatics and Engineering, The University of Electro-Communications |
| October 2015 | Joined Hammock Corporation as a part-time employee | |
| April 2012 | | Entered the Faculty of Informatics and Engineering, The University of Electro-Communications |

## SKILLS HIGHLIGHTS

### Programming Languages

| Language | Experience and Uses |
| --- | --- |
| C# | A primary language in professional work, used for web applications, API servers, and business applications. |
| Rust | A primary language for personal projects, including CLI tools, servers, and systems programming. Also used professionally. |
| Python | Used for utilities in personal projects and for data processing and application development at work. |
| Go | Used professionally to build an authentication and authorization server and a gRPC-based data integration system. |
| C | Used since university, building a foundation in low-level programming and CPU, memory, and cache efficiency. |
| C++ | Used since university for object-oriented programming, template metaprogramming, and SIMD optimization of image processing. |
| TypeScript / JavaScript | Primary languages in professional work, used for frontend development, SSR-based web applications, and Node.js servers. |

### Software Design and Architecture

| Area | Experience and Focus |
| --- | --- |
| Software Architecture | Major web application renewal, designing new structures on an existing foundation and separating responsibilities. |
| API Design | Defining API boundaries and responsibilities; providing requirements and input/output examples and coordinating with developers in other departments. |
| Loose Coupling and Replaceability | Dependency injection (DI), interface-based dependencies, encapsulation, and replaceable components. |
| Testing and Quality Improvements | Introducing unit tests, incrementally refactoring existing code, and improving maintainability. |
| Distributed Systems and Data Integration | gRPC and Protocol Buffers for device communication and streaming data collection. |
| Performance Optimization | SIMD image-processing optimization with PowerPC VMX and performance improvements to existing applications. |

### Cloud Infrastructure

| Category | Experience and Services |
| --- | --- |
| AWS | Used professionally for cloud systems including industrial IoT and remote monitoring of machine tools. |
| Serverless and APIs | Lambda, API Gateway |
| Compute and Delivery | EC2, ELB, CloudFront, Route 53 |
| Storage, Messaging, and Analytics | S3, DynamoDB, SQS, Athena |

### Tools and Development Environment

| Category | Technologies and Tools |
| --- | --- |
| IDEs and Editors | Visual Studio Code, Visual Studio |
| Version Control | Git |
| Containers and Development Environments | Docker, WSL |
| Databases | PostgreSQL, MySQL, SQLite |

---

## WORK EXPERIENCE

### Hammock Corporation (Part-Time)

- Period: October 2015 – March 2018
- Role: Technical Staff (Part-Time)

#### Responsibilities

| Item | Details |
| --- | --- |
| Development Environment | Windows |
| Languages / Frameworks | C# / .NET Framework<br>C++<br>Python |

I tested development versions of OCR software, evaluated recognition accuracy, prepared training data, and researched OCR-related technologies.
I also learned version control with Git.

### Fixstars Corporation (Internship)

- Period: August 2017 – September 2017
- Role: Software Developer (Internship)

#### Project: Image Processing Algorithm Optimization

| Item | Details |
| --- | --- |
| Development Environment | Windows, Linux |
| Languages / Frameworks | C<br>C++ |

I ported image processing algorithms to PowerPC VMX and improved their performance.
Although I was already familiar with SIMD optimization, I learned the importance of unit tests for verifying program correctness.
Since that internship, I have emphasized catching errors at compile time through type systems and writing tests, practices that continue to help me build reliable software.

### Core Concept Technologies Inc.

- Period: April 2018 – November 2021
- Role: Software Engineer

#### Project: Data Collection Application for Machine Tools

| Item | Details |
| --- | --- |
| Period | July 2018 – November 2021 |
| Development Team Members | 2–3 people |
| Development Environment | Windows, Linux |
| Languages / Frameworks | C# / .NET Framework, ASP.NET<br>C++<br>JavaScript / Vue.js |

I developed software that provides a unified interface to machine tools whose protocols and available data vary by manufacturer.
My work included fixing defects, improving performance, and implementing new features.
While fixing defects, I also refactored redundant or difficult-to-read code to improve maintainability without sacrificing performance.

#### Project: Authentication and Authorization Server

| Item | Details |
| --- | --- |
| Period | November – December 2018 |
| Development Team Members | 1 person |
| Development Environment | Windows |
| Languages / Frameworks | Go |

I built an authentication and authorization server to authorize access to a customer's internal applications through Microsoft Azure AD.
Because the existing applications could not be modified, I chose a reverse-proxy architecture.
I selected Go for its mature authentication and authorization libraries, high runtime performance, and ease of learning.

#### Project: IoT Device Monitoring and Visualization System

| Item | Details |
| --- | --- |
| Period | December 2018 – April 2021 |
| Development Team Members | 1–2 people |
| Development Environment | Windows |
| Languages / Frameworks | C# / .NET Framework, ASP.NET<br>JavaScript / Vue.js |

I developed an application that collects, manages, and visualizes data from IoT devices manufactured and sold by a customer.
The first version was created as a demonstration for an IoT trade show.
The customer subsequently commissioned further development, and the application became a product distributed to end users.

To meet the trade show deadline, we prioritized implementation and neglected some requirements analysis and design, accumulating technical debt.
Later, I improved documentation, clarified specifications with the customer, and addressed the debt that needed to be repaid.

#### Project: Remote Management System for Machine Tools

| Item | Details |
| --- | --- |
| Period | March 2019 – November 2021 |
| Development Team Members | 3–4 people |
| Development Environment | Windows, Linux |
| Languages / Frameworks | JavaScript / Vue.js, Node.js<br>C# / .NET Framework, ASP.NET |

For a machine-tool manufacturer, I developed and operated a system for monitoring the operating status and diagnostic information of machines, both within factories and after shipment to end users.
It supported troubleshooting and remote firmware updates.

The system ran on AWS. It stored and transformed data received from the data collection application described above, provided an API server for retrieving data for web interfaces, and hosted those interfaces.
This project introduced me to serverless computing, which made a strong impression on me.

#### Project: Sample Implementation of an Industrial Communication Protocol

| Item | Details |
| --- | --- |
| Period | May – July 2019 |
| Development Team Members | 1 person |
| Languages / Frameworks | C# / .NET Framework |

I developed a sample implementation of MTConnect, an industrial communication protocol, to help a customer in the machine-tool industry gain familiarity with the technology.

#### Project: EMO International Trade Fair

| Item | Details |
| --- | --- |
| Period | July – September 2019 |
| Development Team Members | 1 person |
| Development Environment | Windows |
| Languages / Frameworks | C# / .NET Framework<br>Go<br>TypeScript / Vue.js |

I developed a demonstration application for a customer's exhibition at EMO, an international machine-tool trade fair.
The demonstration used umati, an interface for accessing data from network-connected machine tools.

The application had three components:

- A server that acquires data from machine tools and exposes it through the umati interface
- An intermediary server that accesses the umati server and forwards data to a web interface
- A web interface that displays the data defined by umati

I had limited prior knowledge of the machine tools themselves, so the specification alone did not answer all of my questions.
By working directly with the customer's engineers and exchanging knowledge, I was able to complete the application.

Communicating by email with the event organizer and partner companies also gave me my first opportunity to use English in a professional setting.

#### Project: Data Acquisition Proof of Concept for Predictive Maintenance

| Item | Details |
| --- | --- |
| Period | November 2019 – April 2020 |
| Development Team Members | 5–6 people |
| Development Environment | Windows, Linux |
| Languages / Frameworks | Go / grpc-go<br>C# / .NET Core, ASP.NET Core<br>Rust / tonic, Tokio |

This project explored detecting tool breakage and early warning signs of failure in machine tools operating at a customer's factory.
The system consisted of:

- Devices (sensors and circuit design)
- Data acquisition system
- Web interface for monitoring data
- Data analysis

I was solely responsible for the data acquisition system.
The existing data collection application could not meet the requirements, so I developed a new system from scratch.

The system needed to accommodate new devices or replacements of existing ones, rather than being tied to a specific hardware configuration.
To achieve this, I assigned one gRPC server to each device, had all servers use the same Protocol Buffers definition, and used one gRPC client to stream data from multiple servers.

By defining only the communication interface and data types with gRPC and Protocol Buffers, the design supported flexible combinations of devices and allowed each server to be implemented in a different programming language.

When a new type of device was introduced during the project, the cost of integration remained low—even when the manufacturer's library could only be used from a particular programming language.

#### Project: Architectural 3D Model Viewer

| Item | Details |
| --- | --- |
| Period | January – May 2020 |
| Development Team Members | 3–4 people |
| Development Environment | Windows, Linux |
| Languages / Frameworks | TypeScript, JavaScript / Angular |

I worked on customizing a browser-based 3D model viewer for a customer.
The viewer consisted of:

- A 3D engine
- An architecture-specific abstraction layer (including engine abstractions and APIs for hierarchy information)
- General-purpose GUI components (such as toolbars)

I was responsible for the general-purpose GUI components.

#### Project: Prototype Viewer for Very Large 3D Models

| Item | Details |
| --- | --- |
| Period | May 2020 – November 2021 |
| Development Team Members | 2–3 people |
| Development Environment | Windows, Linux |
| Languages / Frameworks | Rust / Actix, actix-web, Tokio<br>JavaScript / Node.js |

I worked on a prototype viewer for very large 3D models, approximately 10–100 GB, which could not be displayed directly in a web browser using the existing product.

We ran the 3D engine on a high-performance PC with a GPU and transmitted its rendered output to a web interface.
We also provided APIs to relay user interactions from the web interface back to the 3D engine.

The system consisted of:

- A 3D engine
- An API server that mediated interactions between the 3D engine and the web interface
- A web interface that served as sample code using the APIs

I was responsible for the API server and the web interface.

#### Project: Architectural Design Workflow System

| Item | Details |
| --- | --- |
| Period | April – October 2021 |
| Development Team Members | More than 30 people |
| Development Environment | Windows, Linux |
| Languages / Frameworks | C# / .NET Framework<br>TypeScript, JavaScript / Angular |

I participated in developing a system for architectural design workflows.
The system consisted of multiple applications, and I worked on frontend and backend development for one of them.

### Kakaku.com, Inc.

- Period: November 2022 – Present
- Role: Software Engineer

#### Main Responsibilities

| Item | Details |
| --- | --- |
| Period | November 2022 – Present |
| Development Team Members | 4–5 people |
| Development Environment | Windows, Linux |
| Languages / Frameworks | C# / .NET Framework, ASP.NET<br>JavaScript<br>Python |

I develop and maintain web services, including web applications, administration interfaces, and batch-processing applications.

The web applications primarily use server-side rendering (SSR). On the client side, I often work with plain JavaScript rather than UI frameworks such as Vue.js or React.

Although product planning, design, and engineering are separate organizational functions, we work closely and coordinate flexibly. I contribute an engineering perspective to refining requirements and coordinating with designers, with the aim of improving product quality.

I also work on incremental improvements to long-lived codebases. While accounting for existing functionality and operational constraints, I have helped introduce unit tests and dependency injection (DI), separate responsibilities, and refactor code to improve maintainability and ease of change.

#### Project: Major Web Application Renewal

For a major web application renewal, I worked on substantially redesigning the application while retaining established infrastructure such as databases and shared libraries. My responsibilities included software architecture design, refining requirements with product planners, defining API boundaries, and coordinating with developers in other departments.

Extensive documentation helped us understand the existing system and its compatibility requirements. A key design challenge was representing the new application's structures and extensions on top of the existing foundation. I worked closely with product planners to clarify requirements and align them with feasible technical designs.

When defining API boundaries, I considered responsibility separation both within the system and across development teams. For APIs owned by other departments, I provided requirements and concrete input/output examples from the consumer's perspective and collaborated with their developers to refine the interfaces.

For the internal architecture, I applied lessons from introducing DI and separating responsibilities in other web applications. I emphasized dependencies through interfaces to encourage encapsulation and loose coupling, improve unit-testability, and make implementations easier to replace.


---

## LANGUAGES

- Japanese: Native
- English: Intermediate reading and writing

## PERSONAL STATEMENT

### Engineering Principles

I emphasize performance, safety, maintainability, and ease of change when designing and implementing software. Rather than focusing only on delivering features, I aim to build systems that remain maintainable and adaptable over time through clear separation of responsibilities, well-managed dependencies, and appropriate abstractions.

I also value making the reasoning behind a design understandable to other developers, including intended behavior, technical constraints, and trade-offs. When deadlines or compatibility with existing systems prevent an ideal design, I try to make those compromises explicit and leave room for future improvements.

### Continuous Learning

I prefer to deepen my understanding of new technologies and design approaches through hands-on experimentation, alongside reading documentation and technical articles. My personal projects, primarily in Rust, provide opportunities to explore systems programming and software architecture.

Generative AI has reduced the cost of implementation and prototyping, making it practical to try ideas that I previously could not pursue due to time constraints. I use AI not merely to generate code, but also to implement and compare different designs and test technical hypotheses more quickly.

At the same time, I believe that deciding what to design, what to validate, and how to assess trade-offs remains essential. Rather than accepting AI-generated code or designs uncritically, I evaluate them through review, testing, and performance measurements when appropriate, aiming to combine faster experimentation with sound engineering judgment.

## OTHER

- [GitHub](https://github.com/namba3)
- [Technical articles](https://namba3.github.io/commonplace/)
- Member of the [Information Processing Society of Japan (IPSJ)](https://www.ipsj.or.jp/english/index.html)
- Interests: Balcony gardening and houseplants

