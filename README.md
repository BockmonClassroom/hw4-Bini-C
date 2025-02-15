[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hiWoDjT-)
# HW4
HW 4
(Due 2/17)
Part 1 (50 points): Normalization and Standardization 
Take the iris data set and create two new .csv data sets (25 points each). One that normalizes all columns to have values between 0 and 1 and a second that standardizes all columns to have a mean of 0 and standard deviation of 1.
Push both files to github. 

Part 2 (50 points): ER Diagram 
Create an ER diagram that models a zoo:
Define at least three entities that have several attributes for each entity, their relationship between entities, and their constraints. Argue your decisions. You will graded based on your explanation on why you chose certain constraints. 
What to submit 
Either create a markdown readme file that has a copy of your ER diagram and explanation or .pdf version and push that to github.
Please also submit a link to your github submission to Canvas as well. This helps the TA grade faster.


**############################### PART 1  ##################################**

In the Part1, I have performed data preprocessing on the Iris dataset by applying normalization nd standardization techniques to the numerical features of the dataset.

1. NORMALIZATION:
    I scaled the numerical columns of the dataset to a range of 0 to 1. This is done using below formula:
        ![alt text](image.png)

    where Xmin and Xmax are the minimum and maximum values of each column, respectively.
    I have saved the normalized dataset as Normalized_Iris.csv.

    ![alt text](image-1.png)

2. STANDARDIZATION:
    I standardized the dataset to ensure that the numerical columns have a mean of 0 and standard deviation of 1. This is done using below formula:
        ![alt text](image-3.png)

    where μ and σ and the mean and standard deviation of each column, respectively.
    I have saved the normalized dataset as Standardized_Iris.csv.

    ![alt text](image-2.png)




**############################### PART 2  ##################################**

In the Part2, I have created an ER diagram to model a Zoo system. I have defined four main entities: Animal, Enclosure, Show, and Visitor.
Each of these entities has several attributes, and I’ve defined their relationships with appropriate cardinality and constraints.

**Visitor to Show (attends):**
In my zoo system, there are a total of five shows happening per day, each at a different time. Thus, the StartTime attribute in the Show entity is kept unique to avoid any scheduling conflicts. A visitor is allowed to attend up to five shows in a day. Additionally, a show cannot happen without at least five audience members(visitors), and the maximum capacity is 30 visitors to maintain comfort and crowd control.

Thus, I created a many-to-many relationship between Visitor and Show, as one visitor can attend multiple shows, and a show can have multiple visitors.
The cardinality constraint ensures that a visitor can attend 0 to 5 shows, and each show can have between 5 and 30 visitors.

**Animal to Show (participates in):**
In my zoo system, we want to ensure that animals are not overworked. Hence, an animal can only participate in 0, 1, or 2 shows per day. A show could have either at least one animal but no more than 10 animals to avoid overcrowding. For example, a dolphin show can feature one or a group of up to ten dolphins.

Thus, I created a many-to-many relationship between Animal and Show, as animals can participate in multiple shows, and each show can feature multiple animals.
The cardinality constraint ensures an animal can participate in 0 to 2 shows, and each show can have between 1 to 10 animals.

**Visitor to Enclosure (visits):**
The zoo has 200 enclosures in total, and visitors are free to explore as many enclosures as they like during their visit. However, up to 25 visitors can visit one enclosure at a time to prevent overcrowding outside the enclosure.

Thus, I created a many-to-many relationship between Visitor and Enclosure, as a visitor can visit multiple enclosures, and each enclosure can have multiple visitors.
The cardinality constraint ensures that a visitor can visit between 0 and 200 enclosures, and up to 25 visitors can visit each enclosure.

**Animal to Enclosure (resides in):**
The zoo has a variety of enclosure sizes, each having different capacities. So, an enclosure can house up to 7 animals, depending on the size of the enclosure and the species. Each animal resides in exactly one enclosure.

Thus, I created a one-to-many relationship between Enclosure and Animal, as each animal can reside in only one enclosure, but each enclosure can house multiple animals. The cardinality constraint ensures the same.

**Other constraints:**

_Primary Key Constraints:_ Each entity has a primary key (VisitorID, AnimalID, ShowID, EnclosureID) to ensure that each record is uniquely identifiable and avoid duplicates.

_Unique Constraints:_ PhoneNumber in Visitor is unique to prevent duplicate contact information. StartTime in Show is unique to avoid conflicts in show schedules.

_Optional Attributes:_ email in Visitor is an optional attribute, which means that it is not required for every visitor. Some visitors may not provide an email address, and its value can be NULL.

_Multi-valued Attributes:_ PhoneNumber in Visitor is a multi-valued attribute, meaning a visitor can have multiple phone numbers.

_Foreign Key Constraints:_ While foreign keys are not explicitly shown in the ER diagram, they play an important role in linking entities in the database. The EnclosureID in the Animal entity would act as a foreign key, linking each animal to its specific enclosure. Similarly, the VisitorID and ShowID would be used to link Visitor and Show, and the AnimalID and ShowID would link Animal and Show.

![HW4_Part2 (3)](https://github.com/user-attachments/assets/f674e85f-888f-4482-bab5-e7bb40f4c08c)

