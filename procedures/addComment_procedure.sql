alter PROCEDURE AddComment
	@commenter bigint,
	@PostID INT,
 @CommentText NVARCHAR(MAX)
   
	
AS
BEGIN
	  DECLARE @commentDate DATETIME;
	 SET @commentDate = GETDATE();

INSERT INTO Comment 
    VALUES (@commenter, @PostID, @commentDate, @CommentText);
END


