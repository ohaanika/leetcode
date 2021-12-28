# [Systems Analysis and Design](https://www.goodreads.com/book/show/22505475-systems-analysis-design)

## Table of Contents

8. [Architecture Design (pgs 237-264)](#8-architecture-design)
	- [x] Introduction
	- [ ] Elements of an Architecture Design
		- [x] [Architectural Components](#architectural-components)
		- [x] [Client-Server Architectures](#client-server-architectures)
		- [x] [Client-Server Tiers](#client-server-tiers)
		- [ ] [Server-Based Architecture](#server-based-architecture)
		- [ ] Mobile Application Architecture
		- [ ] Advances in Architecture Configurations
		- [ ] Comparing Architecture Options
	- [ ] Creating an Architecture Design
		- [ ] Operational Requirements
		- [ ] Performance Requirements
		- [ ] Security Requirements
		- [ ] Cultural and Political Requirements
		- [ ] Designing the Architecture
	- [ ] Hardware and Software Specification
	- [ ] Applying the Concepts at Tune Source
		- [ ] Creating an Architecture Design
		- [ ] Hardware and Software Specification
	- [ ] Chapter Review

## 8. Architecture Design

### Objectives
- Describe the fundamental components of an information system.
- Describe *client–server*, *server-based*, and *mobile application* architectures.
- Describe how *cloud computing* can be incorporated as a system architecture component.
- Explain how *operational*, *performance*, *security*, *cultural*, and *political requirements* affect the architecture design.
- Create a hardware and software specification.

### Architectural Components
- Four main functions of software systems:
	1. **Data storage** - Most information systems require data to be stored and retrieved.
	2. **Data access logic** - The processing required to access data, often meaning database queries in Structured Query Language (SQL). 
	3. **Application logic** - The logic documented in the DFDs, use cases, and functional requirements.
	4. **Presentation logic** - The display of information to the user and the acceptance of the user’s commands (the user interface).
- Three main hardware components of a system:
	1. **Clients** - The input–output devices employed by the user (e.g. desktop or laptop computers, handheld devices, smartphones, tablet devices, special-purpose terminals)
	2. **Servers** - Typically larger multi-user computers used to store software and data that can be accessed by anyone who has permission.
	3. **Network** - Connects the computers.

### Client-Server Architectures
- Client/Server responsibilities in relation to four functions of software systems:
	- Client is for **presentation logic**.
	- Server is for **data storage** and **data access logic**.
	- Client/Server is for **application logic**.
		- **Thick/Fat** client contains *more* application logic.
		- **Thin** client contains *less* application logic.
			- Popular because lower overhead and easier maintenance.
				- e.g. Web-based systems are designed with the Web browser performing presentation and only minimal application logic using such programming languages as JavaScript, while the server side has most of the application logic, all of the data access logic, and all of the data storage.
- Advantages:
	- They are scalable.
		- You can increase/decrease the storage and processing capabilities of the servers.
		- You can add another server if one becomes overloaded.
	- They support many different types of clients and servers.
		- **Middleware** is a type of system software designed to translate between different vendors’ software.
	- For thin client–server architectures that use Internet standards, you can clearly separate the presentation logic, the application logic, and the data access logic, and design each to be somewhat independent.
	- If a server fails, only the applications requiring that server will fail. The failed server can be swapped out and replaced and the applications can then be restored.
- Disadvantages:
	- Writing software for both client and server side is more complicated than writing all-in-one software.
	- Updating the system with new version of software is extensive. 

### Client-Server Tiers
- Various ways application logic can be partitioned between client and server:
	- **2-tiered** (2 sets of computers):
		- Client - Handles presentation logic and application logic.
		- Server - Handles data access logic and data storage.
	- **3-tiered** (3 sets of computers):
		- Client - Handles presentation logic.
		- Application server(s) - Handles application logic.
		- Database server(s) - Handles data access logic and data storage.
	- **n-tiered**:
		- Similar to 3-tiered, but where the application logic (middle tier) is distributed among multiple layers of *more specialized server computers*.
		- Example of Web-based e-commerce systems:
			- Client - Handles presentation logic.
			- Web server(s) - Handles Web-related application logic.
				- Receive HTTP requests from client to view pages from the Web server(s).
				- Respond with HTML documents to enable to user to view merchandise for sale.
			- Application server(s) - Handles other application logic.
				- Allow the user to put items in a shopping cart.
				- Determine item pricing and availability.
				- Compute purchase costs, sales tax, and shipping costs.
				- Authorize payments.
			- Database server(s) - Handles data access logic and data storage.
		- Advantages:
			- It separates out the processing that occurs to better balance the load on the different servers; it is more scalable.
				- In the n-tiered example, we have three separate server types, a configuration that provides more power than if it was 2-tiered with only one server. 
				- If the application server is *heavily loaded*, we can replace it with a more powerful server or just put in several more application servers to share the load. 
				- If the database server is *underused*, we could store data from another application on it.
		- Disadvantages: 
			- The configuration puts a greater load on the network. The n-tiered model requires more communication among the servers. It generates more network traffic, so you need a higher-capacity network. 
			- It is more difficult to program and test software in n-tiered than in 2-tiered, because more devices have to communicate properly to complete a user’s transaction.

### Server-Based Architecture
- Partition:
	- Terminal - Enables users to send and receive messages to and from server.
	- Server - Handles presentation logic, application logic, data access logic and data storage.
