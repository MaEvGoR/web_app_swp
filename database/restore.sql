SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE AnswerOption
(
 SurveyID       integer NOT NULL,
 Text           varchar(100) NOT NULL,
 QuestionNumber integer NOT NULL,
 OptionNumber   integer NOT NULL,
 CONSTRAINT PK_Option_of_answer PRIMARY KEY ( SurveyID, QuestionNumber, OptionNumber )
);

CREATE INDEX fkIdx_82 ON AnswerOption
(
 QuestionNumber,
 SurveyID
);


CREATE TABLE Answer
(
 FilledSurveyID integer NOT NULL,
 AnswerNumber   integer NOT NULL,
 Type           integer NOT NULL,
 ChosenOption   integer NULL,
 AnswerText     varchar(200) NULL,
 CONSTRAINT PK_Answer PRIMARY KEY ( FilledSurveyID, AnswerNumber )
);

CREATE INDEX fkIdx_71 ON Answer
(
 FilledSurveyID
);

CREATE TABLE DOEmember
(
 UserID integer NOT NULL,
 CONSTRAINT PK_DOE_member PRIMARY KEY ( UserID )
);

CREATE INDEX fkIdx_21 ON DOEmember
(
 UserID
);

CREATE TABLE Course
(
 CourseID    integer NOT NULL,
 Name        varchar(50) NOT NULL,
 ProfessorID integer NOT NULL,
 CONSTRAINT PK_Course PRIMARY KEY ( CourseID )
);

CREATE INDEX fkIdx_25 ON Course
(
 ProfessorID
);

CREATE TABLE Question
(
 SurveyID       integer NOT NULL,
 QuestionNumber integer NOT NULL,
 Type           integer NOT NULL,
 QuestionText   varchar(250) NOT NULL,
 CONSTRAINT PK_table_20 PRIMARY KEY ( QuestionNumber, SurveyID )
);

CREATE INDEX fkIdx_56 ON Question
(
 SurveyID
);

CREATE TABLE FilledSurvey
(
 FilledSurveyID        integer NOT NULL,
 ConstrainedBySurveyID integer NOT NULL,
 CONSTRAINT PK_Filled_Survey PRIMARY KEY ( FilledSurveyID )
);

CREATE INDEX fkIdx_67 ON FilledSurvey
(
 ConstrainedBySurveyID
);


CREATE TABLE Survey
(
 SurveyID         integer NOT NULL,
 Name             varchar(50) NOT NULL,
 CreationTime     timestamp NOT NULL,
 ExpirationTime   timestamp NOT NULL,
 Description      varchar(500) NULL,
 ConsideredUserID integer NOT NULL,
 CONSTRAINT PK_Survey PRIMARY KEY ( SurveyID )
);

CREATE INDEX fkIdx_91 ON Survey
(
 ConsideredUserID
);

CREATE TABLE StudentOfTheCourse
(
 StudentID integer NOT NULL,
 CourseID  integer NOT NULL,
 CONSTRAINT PK_Student_of_the_course PRIMARY KEY ( StudentID, CourseID )
);

CREATE INDEX fkIdx_28 ON StudentOfTheCourse
(
 StudentID
);

CREATE INDEX fkIdx_38 ON StudentOfTheCourse
(
 CourseID
);

CREATE TABLE SystemUser
(
 UserID  integer NOT NULL,
 Mail    varchar(50) NOT NULL,
 Hash    varchar(30) NOT NULL,
 Name    varchar(15) NOT NULL,
 Surname varchar(15) NOT NULL,
 CONSTRAINT PK_User PRIMARY KEY ( UserID )
);

CREATE TABLE TeacherAssistantOfTheCourse
(
 CourseID           integer NOT NULL,
 TeacherAssistantID integer NOT NULL,
 CONSTRAINT PK_TeacherAssistant_of_the_course PRIMARY KEY ( CourseID, TeacherAssistantID )
);

CREATE INDEX fkIdx_381 ON TeacherAssistantOfTheCourse
(
 CourseID
);

CREATE INDEX fkIdx_47 ON TeacherAssistantOfTheCourse
(
 TeacherAssistantID
);

CREATE TABLE UserFillInSurvey
(
 UserID   integer NOT NULL,
 SurveyID integer NOT NULL,
 CONSTRAINT PK_UserFillInSurvey PRIMARY KEY ( UserID, SurveyID ),
 CONSTRAINT FK_100 FOREIGN KEY ( UserID ) REFERENCES SystemUser ( UserID ),
 CONSTRAINT FK_103 FOREIGN KEY ( SurveyID ) REFERENCES Survey ( SurveyID )
);

CREATE INDEX fkIdx_100 ON UserFillInSurvey
(
 UserID
);

CREATE INDEX fkIdx_103 ON UserFillInSurvey
(
 SurveyID
);

--Constraints:
ALTER TABLE only AnswerOption
 ADD CONSTRAINT FK_82 FOREIGN KEY ( QuestionNumber, SurveyID ) REFERENCES Question ( QuestionNumber, SurveyID );


ALTER TABLE only Answer
 ADD CONSTRAINT FK_71 FOREIGN KEY ( FilledSurveyID ) REFERENCES FilledSurvey ( FilledSurveyID );


ALTER TABLE only DOEmember
 ADD CONSTRAINT FK_21 FOREIGN KEY ( UserID ) REFERENCES SystemUser ( UserID );

ALTER TABLE only Course
 ADD CONSTRAINT FK_25 FOREIGN KEY ( ProfessorID ) REFERENCES SystemUser ( UserID );

ALTER TABLE only Question
 ADD CONSTRAINT FK_56 FOREIGN KEY ( SurveyID ) REFERENCES Survey ( SurveyID );

ALTER TABLE only FilledSurvey
 ADD CONSTRAINT FK_67 FOREIGN KEY ( ConstrainedBySurveyID ) REFERENCES Survey ( SurveyID );

ALTER TABLE only Survey
 ADD CONSTRAINT FK_91 FOREIGN KEY ( ConsideredUserID ) REFERENCES SystemUser ( UserID );

ALTER TABLE only StudentOfTheCourse
 ADD CONSTRAINT FK_28 FOREIGN KEY ( StudentID ) REFERENCES SystemUser ( UserID );
ALTER TABLE only StudentOfTheCourse
 ADD CONSTRAINT FK_38 FOREIGN KEY ( CourseID ) REFERENCES Course ( CourseID );

ALTER TABLE only TeacherAssistantOfTheCourse
 ADD CONSTRAINT FK_38 FOREIGN KEY ( CourseID ) REFERENCES Course ( CourseID );
ALTER TABLE only TeacherAssistantOfTheCourse
 ADD CONSTRAINT FK_47 FOREIGN KEY ( TeacherAssistantID ) REFERENCES SystemUser ( UserID );