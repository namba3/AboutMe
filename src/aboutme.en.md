# ABOUT ME

## SUMMARY

- Professional experience as a software engineer
  - Three years of experience with IoT-related systems
  - More than four years of experience developing web services
- Three years of part-time experience as a technical staff member, primarily on OCR-related projects
- A foundation in computer science
- Some experience with data science
- Experience developing frontend, backend, and microservice software

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

#### C#

One of the main languages used in my current and previous jobs.
I have developed applications and API servers using C#.

#### Rust

I began studying Rust in earnest around the announcement of Rust 2018 Edition.
I believe it will play an important role in the future of systems programming.

Rust is one of my primary languages for personal projects, mainly command-line tools and small servers.
I also have experience developing small applications with Rust professionally.

#### Python

One of my primary languages for personal projects, mainly small utilities.
I have also used Python professionally for basic data processing.

#### Go

I used Go to build an authentication and authorization server in one project.
I also favored Go when adopting gRPC in another project.
I have followed Go less closely since I began working with Rust.

#### C

I have used C since my student years.
It helped me develop an understanding of CPU efficiency, memory efficiency, and cache performance.
I have followed C less closely since I began working with Rust.

#### C++

I have used C++ since my student years.
I learned object-oriented programming and template metaprogramming through C++.
I kept up with C++11, C++14, C++17, and C++20.
I have followed C++ less closely since I began working with Rust.

#### TypeScript / JavaScript

One of the main language families used in my current and previous jobs.
Most of my experience is in frontend development, but I have also developed servers with Node.js.

### Cloud Infrastructure

#### AWS

AWS was the primary cloud platform in my previous job.
I used it across several projects, including the following services:

- Lambda, API Gateway, EC2, S3, DynamoDB, SQS, Athena, CloudFront, Route 53, ELB

### Tools and Technologies

- IDEs / editors: VS Code, Visual Studio
- Version control: Git
- Virtualization and containers: Docker, WSL
- Database systems: PostgreSQL, MySQL, SQLite

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

I develop and maintain web services, working across a broad range of components, including related administration interfaces and batch-processing applications.


---

## LANGUAGES

- Japanese: Native
- English: Intermediate reading and writing

## OTHER

- [GitHub](https://github.com/namba3)
- [Technical articles](https://namba3.github.io/commonplace/)
- Member of the [Information Processing Society of Japan (IPSJ)](https://www.ipsj.or.jp/english/index.html)
- Interests: Balcony gardening and houseplants

## PERSONAL STATEMENT

### Engineering Principles

I aim to design safe and efficient algorithms, with an emphasis on software quality.
Whenever possible, I write documentation comments to make code easier to understand and help new team members become productive.
When deadlines take priority over safety or runtime performance, or when code may contain defects, I document those limitations so the code can be refactored more easily later.

### Continuous Learning

I regularly explore new technologies and experiment with those that interest me.
I have followed developments in WebAssembly and WASI, the system interface for WebAssembly runtimes.
I am comfortable reading technical articles in English and actively seek information on topics that are not well covered in Japanese.
