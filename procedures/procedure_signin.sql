--signin query


alter PROCEDURE Signin
    @email NVARCHAR(255),
     @password NVARCHAR(100)
AS
BEGIN
 DECLARE @error_message NVARCHAR(100) = 'User not found.';
    
DECLARE @userExists INT = 0;
    DECLARE @isPasswordCorrect INT = 0;

    -- Check if user1 exists
SELECT @userExists = COUNT(*)
    FROM [User1]
WHERE email = @email;

    -- If user exists, check if password is correct
IF @userExists = 1
BEGIN
-- Ideally, passwords should be hashed, and a proper password verification function should be used.
-- For this example, we'll assume passwords are stored in plain text (not recommended for production use).
SET @isPasswordCorrect = (SELECT COUNT(*) FROM [User1] WHERE email = @email AND password = @password);
    END
-- Return success or failure message
IF @userExists = 1 AND @isPasswordCorrect = 1
BEGIN
SELECT 'Success: User signed in successfully!' AS 'Message';
    END
ELSE
BEGIN
   RAISERROR(@error_message, 16, 1);
    END
END


