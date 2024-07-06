USE [muzmusic]
GO
/****** Object:  StoredProcedure [dbo].[InsertPost]    Script Date: 7/5/2024 12:43:09 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- POST PUBLISH Q

ALTER PROCEDURE [dbo].[InsertPost]
    (@title NVARCHAR(100),
     @content NVARCHAR(MAX),
     @image_address NVARCHAR(255),
     @category NVARCHAR(100),
	 @author_id bigint)
AS
BEGIN
-- Variable declaration

    -- Assign current user's ID to @author_id variable
-- Replace 'author_column_name' with the actual column name in your User table

    -- Validation
IF (SELECT COUNT(*) FROM Category WHERE Category_Name = @category) = 0
BEGIN
RAISERROR('Invalid category provided', 16, 1);
        RETURN;
    END
-- Insert the new post
INSERT INTO Post (Title, Content, [Image], author, category,published_date)
    VALUES (@title, @content, @image_address,@author_id,
            (SELECT Id FROM Category WHERE Category_Name = @category),GETDATE());
END;



