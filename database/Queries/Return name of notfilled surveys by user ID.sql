SELECT Survey.Name as SurveyName
FROM Survey
     WHERE Survey.SurveyID NOT IN (SELECT SurveyID
         FROM UserFillInSurvey
         --Change on required id
         WHERE UserID = 3);