alter PROCEDURE SearchPosts
    @searchString NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT p.id,p.title,p.content,c.category_name,u.first_name
    FROM post as p join Category as c on c.id=p.category join user1
	as u on u.id=p.author 
    WHERE title LIKE CONCAT('%', @searchString, '%') OR content LIKE CONCAT('%', @searchString, '%');
END


