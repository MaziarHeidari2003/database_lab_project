alter PROCEDURE Signup
    (@password NVARCHAR(255),
     @email NVARCHAR(255),
     @first_name NVARCHAR(100),
     @last_name NVARCHAR(100),
     @bio TEXT,
     @image NVARCHAR(255))
AS
BEGIN
-- Check for @ character in email
IF (@email NOT LIKE '%@%')
    BEGIN
-- Raise an error if no @ character is found in the email
RAISERROR('Invalid email format!', 16, 1);
    END
ELSE
BEGIN TRY
        -- Clean data before insertion
SET @password = LTRIM(RTRIM(@password));
        SET @email = LTRIM(RTRIM(@email));
        SET @first_name = LTRIM(RTRIM(@first_name));
        SET @last_name = LTRIM(RTRIM(@last_name));
        --SET @bio = LTRIM(RTRIM(@bio));
        SET @image = LTRIM(RTRIM(@image));

        -- Insert cleaned data into the User1 table
INSERT INTO "User1" (password, email, first_name, last_name, bio, image)
        VALUES (@password, @email, @first_name, @last_name, @bio, @image);
    END TRY
    BEGIN CATCH
        -- Handle any errors that occur during the insertion
PRINT 'An error occurred during signup: ' + ERROR_MESSAGE();
    END CATCH
END















