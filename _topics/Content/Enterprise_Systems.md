---
name: Enterprise Systems
tag: Miscellaneous
layout: page
---

A collection of notes on enterprise software systems, concerned with the development lifecycle of such systems, and their various types.

## SDLC
> Software Development Lifecycle

Every phase in the SDLC has a deliverable, the five phases are as follows:

- Planning : *preliminary investigation report*
- Analysis : *System requirements*
- Design : *DFD's and other reports*
- Implementation : *The new system*
- Security and Support : 


## Systems Planning

Deliverable: preliminary investigation report

The Systems planning process defines the following steps:
- Systems Request
- Justification & SWOT
- Preliminary Investigation
- Evaluation
- Deliverable

| Phase              | Steps | Purpose                                                      |
| ------------------ | ----- | ------------------------------------------------------------ |
| Business Case      | 1-3   | Describe, justify, and evaluate a new system's fiscal impact |
| System Development | 4 - 5 | Develop, test, and evaluate a new system                     |


### System Request

>  A formal approach for new software development

A system request is generally based on one of the following needs:

- More support
- Improved service
- Better performance
- More information
- Reduced cost
- Stronger controls



### Strategic Planning

> A method to justify the development of a new system

Identifying long term goals for an organisation 

- Catalyst for proposing development
- Uses SWOT
- Identifies strengths and how to use them
- Identifies weaknesses and how to reduce them
- Identifies opportunities and how to take advantage of them
- Identifies threats and how to asses, manage, and respond to them 



### Preliminary Investigation

> A preliminary investigation is formed by assessing the feasibility of a project.

 A preliminary investigation considers the:

- Economical feasibility
- Do our benefits outweigh costs
- Operational feasibility
- Will it be easy to use
- Technical feasibility
- Do we have the technical      capability
- Schedule feasibility
- Do we have enough time

 **This report is evaluated by a systems review committee.**


## Systems Analysis
Deliverable: System requirements document

The systems analysis phase defines the following steps:
- Review Feasibility
- Model Requirements
- Consider strategies
- Plan transition to design

### Requirements
We consider these factors when analysing our requirements:
1. Processes
2. Inputs
3. Outputs
4. Performance
5. Control/Security

We then use DFDs to visualise this data. This informs our documentation and development.

### Strategies
IT department’s goal is to deliver the best possible information system, at the lowest possible cost, in the shortest possible time. 

- **JAD** (Joint Application Development), which is user-oriented technique for fact- finding and requirements modelling. It’s not linked to a specific development methodology, systems developers use JAD whenever group input and interaction are desired. 

- **RAD** (Rapid Application Development) in which users involved every step of the way. RAD provides a fast-track approach to a full spectrum of system development tasks, including planning, design, construction and implementation. 

- **Agile** is a method which has intense interaction between system developer and users. 

Techniques Used to gather information include:
- Observation
- Interview
- Questionnaires and surveys
- Reviewing documents



## Systems Implementation
> Developing the system from requirements form the previous phase.

### Traditional Methods of application development
Traditional development usually follows the following structure:
- Plan
- Develop
- Design Modules
- Code Modules
- Test Modules
- Document Modules
- Integration Testing
- System Testing
- Documentation

### Agile Methods:
> Agile is a specific process management method developed for IT

Agile methods compare the result of implementation against the requirements of the system, in a continuous refinement loop

### Tools:
We use tools to orientate the development around a design. This allows us to assess whether we will meet the requirements efficiently.
- DFD
- ERD
- Pseudocode
- Decision Trees

### Testing the system
- Systems are divided into units (individual development groups)
- We test individual units
- If it passes we integrate multiple units and test again
- Once all units are integrated we test the system as a whole
- We try to identify data correctness, execution errors (crashes), boundary, expected, and out of range numerical values
- Ensure the staff has access to documentation
- Demonstrate user interaction
- Verify integration

### Documentation
- Describes a system
- Helps people interacting with the system
- Cuts costs, reduces system downtime, makes maintenance easier

**There are four types of documentation:**
- Program
	- Describes inputs, outputs, logic
	- starts from analysis
	- guides programmers
- System
	- Describes system functions and implementations
	- Includes DFD's etc.
	- Supports maintenance
	- Used when there are errors
- Operations 
	- Used if the system is on a centralized computer
	- for IT people
- User
	- Instructions for system users    

### Data Conversion
When implementing a new system it should consider how to convert old formats of data. Old and new data must be in compatible formats 

### System Changeover
The process of how we begin deploying the new system

| Name     | Characteristics       | Description                                                  |
| -------- | --------------------- | ------------------------------------------------------------ |
| Parallel | Low risk              | Using both systems at the same time                          |
| Cut off  | Lowest cost           | Immediately using the new system                             |
| Pilot    | Lower risk & cost     | Operate at reduced loads on the new system initially         |
| Phased   | Lower cost & low risk | Gradually increase the load at which the new system runs over time |

**Post Implementation We evaluate and produce a final report, covering modifications and enhancements in the future. **



## Systems Security & Support

An On-going phase
- The deliverable for this phase is an operational system
  - Maintained
  - Supported
  - Secured
- We want to make sure everyone is using the system properly
  - No errors
  - Handling security issues
  - Running diagnosis for data integrity
  - Preventing it form becoming obsolete 

### Maintenance

 **Corrective** (high initial and later life cost, low cost during operation)
- Diagnoses and corrects minor errors
- Patching a system failure
- After patching the development team will design a permanent solution 

**Adaptive** (Low initial cost, moderate     to high thereafter - depending on enhancements)

- Enhance the system, making it easier to use
 - Anything that stops the normal operation of a business is the most important concern

**Perfective** (low to moderate costs)

**Preventative** (low to moderate costs)

- Analysing areas of concern
- Preventing system failures
- Increases satisfaction
- Decreased downtime
- Reduced cost of ownership

### Key Activities
- Maintenance requests
- Version Control
- Fault management
- Logging
	- Diagnosis
	- Corrective action
- Workload measurement
	- Benchmarking

### Testing

| Name                      | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| Unit Testing              | Testing individual components                          |
| Integration               | Testing the connectivity between modules               |
| Testing dependant systems | Testing modules dependant on one another               |
| System Testing            | Testing the combination of features that make it whole |



## Backup Systems

| Name         | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| Full         | backup of every file in the system (at the end of the day)   |
| Differential | backup only files that are new or changed since the last full backup |
| Incremental  | includes recent files that never have been backed up         |
| Continuous   | real time streaming method that records all system activity as it occurs |



## Data Flow Diagrams

> Diagrams representing the flow of data between modules and processes

| Level   | Description                                                  |
| ------- | ------------------------------------------------------------ |
| Context | The relationship between business entities                   |
| High    | A detailed breakdown of the process relating entities together |
| Low     | A detailed breakdown of individual processes often broken into multiple applications |



## Transaction Processing Systems

An organised collection of people, procedures, software, databases, and devices used to record completed business transactions.

- Simple processing 
- Extensive data 
- Little decision support
- Highly routine

 ### Importance

- A TPS processes data to update records on business operations, regarding accounts payable, orders, inventory and sales. 
- Reflects the current state of the organisation.
- A TPS provides underlying input to other systems.

 ### Characteristics

- Data is split into **two databases**
  - Operational - current years transactions
- Data warehouse - historical transactions
- A TPS provides CRUD functionality
  - Create Read Update Delete
  - In addition it calculates and summarises transactions
- Outputs reports based on extended CRUD architecture
- Can provide better service
  - [high] Throughput: amount of data processed
  - Available all the time, [highly] accurate
  - Standardised manipulation (reduces unintended processes/mutation of data)

**An automated TPS enables a system to do business with customers**

### Transactions

An event to produce data for a database. **Transactions consist the flow of data that makes analytical and business systems functional.**

- Transactions are isolated,     modular, single units of work
- Transactions are processes     invoked by a user or other modules of a system

 **All TPS have 6 common activities**

1. Collection
2. Editing (Convert to correct data form)
3. Correction (Fixing errors preventing editing)
4. Processing
5. Storage
6. Data Production and reports


## Enterprise Resource Planning

A set of integrated programs that manage a company’s vital business operations for an entire organization

- Integrates all departments through an organization
- Can view enterprise wide information
- Provides a competitive advantage with an integrated single database
- Provides routine functions and decision making
- Not confined to a location
- Developed by large service providers (SAP, Microsoft)

###  Modules
>  A module groups several programs together.

Common modules include:

- Supply chain management
- Sales forecasting
  - Takes demand and inventory to calculate production needs
  - Purchasing & Production planning
- Customer Relationship Management
  - Manages marketing, sales, distribution, accounting, and customer service
  - Anticipate needs of customers
  - Automates these functions
- Accounting
  - Finance
    - Records and documents transactions for statements
  - Managerial
    - provides data to enable strategies for future or current operations
    - Maintains general ledger
    - Tracks associations of records (flow on effect)

### Pros

- Improves access to data
- Quicker customer service
- Quicker decision making
- Improves work processes
  - Vendors development > best practice for business tasks > competitive performance
- Eliminates legacy systems
  - Eliminates multiple systems
- Transitions with changing workforce
- Reduces maintenance costs

### Cons
- Expensive
	- To address this we can modularize the system, and only incorporate needed parts
- Difficult to integrate



## Management information systems

- An integrated collection of people, procedures, and databases which provide information to management to achieve organization goals.
- An MIS is critical for effective decision making, solving problems that arise. These decisions     can be automated.

### Benefits

- Problem Solving
- Enhancing Decision Quality
Difference between TPS
- Advanced calculations and analytics (algorithms)
  - The data collected from TPS informs **decisions made by the MSS**

### Inputs

- Internal data sources
  - TPS and ERP systems
  - Data warehouses
- External Data sources
  - Customer data
  - Internet

### Outputs

- Reports
  - Seduled report
  - Individual reports for big customers produced every month for example.
- Key indicator report
  - Reports on critical activities that are seen to be indicators of the business prosperity. 
  - Provides quick corrective measures to sets of data (like inventory levels).
- Demand report
  - Reports based on a specific request for information
- Exception report
  - Automatically produced reports when unusual situations are detected.
- Drill-down report
  - Produces increasingly detailed reports on specific areas.

### Characteristics of reports

- Hard copy or soft copy
  - Either can be produced by the system
- Fixed and standard formats
- Uses internal data stores inside a system
- User developed
  - Develop programs to query database information
- Information System reports
  - Requires a user request, producing reports for several people

### Types of System

**An MIS system has a specific department, each one generates different types of report specific to that area**

1. Finance
2. Marketing
3. Manufacturing
4. Human Resources

Whilst inputs remain the same across systems, the different outputs are produced by different subsystems. For instance marketing systems will have sales analysis, this may not be present in a manufacturing system.

## Decision Support Systems

### Difference between MIS and DSS

DSS provides structure to unstructured, Abstract problems. They provide information to inform a decision. **A DSS is more intelligent and involves a lot of analytics.** 

> Unstructured problems : A problem who's metrics can not be define in advance

 ### Characteristics

- Provides fast access to information
  - Instantly shows information on performance indicators
  - Realtime interface
  - Can show historical trends
  - **Enables information to make an instant decision**
- Handle large amounts of data
  - Access to databases and intranet, and internet
  - **Provides reliable information**
- Provides report flexibility
  - Can create graphs etc, text and graphics
- Perform statistics analysis
  - Can use python, r, etc.
  - **Provides confidence**
- Supports optimisation
	- Supports all types of decision making
- Simulation
	- Duplicates features of a real system and uses probability to scrutinize data



## Business Intelligence

A wide range of technologies to manipulate data. This provides better understanding of current business performance, revealing new business patterns and relationships. It can also forecast future business results.

**The goal of BI is to get the most value out of information to present analytics in an understandable way.**

### Pros 

- Detect Fraud
- Improve forecasting
- Increase sales
- Optimise operations
- Reduce costs

### BI Tools

- Computer Programming
  - Python
  - MatLab
  - R
- Spreadsheets
  - Importing data to perform operations on, storage of information.
- Querying
  - Presenting data: formatted data, graphs, charts.
- Data visualization
  - Visual depictions of data
- OLAP
  - Online analytical processing, analysing multidimensional data to identify trends and      opportunities.
- Drill-Down analysis
  - Increasingly detailed reports on data (**breaking data into it's components**)
- Data Mining
  - Exploring large amounts of data


## Knowledge Information Systems

A Knowledge Information System is categorized as an expert system.

 ### Expert Systems

- Diagnose problems
- Improve Quality
- Predict Future Events

**Expert Systems are made of:**

- User interfaces
  - Talks to the user
-  Knowledge bases
  - Knowledge acquisition facility
  - The physical knowledge base
  - Talks to the experts
- Inference engines (search engines matching query)
  - The physical Inference engine
- Explanation facility

*Expert systems contain human expert knowledge in a specific area. They replicate problem solving. Draw inference from rules, facts, and relationships.* 

### Knowledge Bases

Data in a knowledge base is:

- Created
- Stored
- Shared
- Used

A **knowledge acquisition facility** is used to input knowledge into the system from users

### Inference Engine

- An inference engine matches user queries to expert knowledge.
- An inference engine incorporates an **explanation facility** to justify how it matched relationships.
- Provides predictions, answers, and suggestions based on testing conclusions based on related facts.

### User Interface Engine

- Facilitates the use of decisions, inference, and knowledge in the system