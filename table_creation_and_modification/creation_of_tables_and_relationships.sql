CREATE TABLE "Reply"(
    "id" BIGINT NOT NULL,
    "replier" BIGINT NOT NULL,
    "parent_comment" BIGINT NOT NULL,
    "content" TEXT NOT NULL,
    "published_date" DATE NOT NULL

);
ALTER TABLE
    "Reply" ADD CONSTRAINT "reply_id_primary" PRIMARY KEY("id");
CREATE TABLE "Category"(
    "category_name" NVARCHAR(100) NOT NULL,
    "id" BIGINT NOT NULL
);
ALTER TABLE
    "Category" ADD CONSTRAINT "category_id_primary" PRIMARY KEY("id");
CREATE TABLE "User1"(
    "id" bigINT NOT NULL,
    "password" NVARCHAR(30) NOT NULL,
    "email" NVARCHAR(255) NOT NULL,
    "bio" TEXT NULL,
    "first_name" NVARCHAR(100) NOT NULL,
    "last_name" NVARCHAR(100) NOT NULL,
    "image" NVARCHAR(255) NULL
);
ALTER TABLE
    "User1" ADD CONSTRAINT "user_id_primary" PRIMARY KEY("id");
CREATE TABLE "Post"(
    "id" BIGINT NOT NULL,
    "title" NVARCHAR(50) NOT NULL,
    "content" TEXT NOT NULL,
    "image" NVARCHAR(255) NOT NULL,
    "author" BIGINT NOT NULL,
    "category" BIGINT NOT NULL,
    "likes" BIGINT NOT NULL,
    "published_date" DATE NOT NULL
);
ALTER TABLE

    "Post" ADD CONSTRAINT "post_id_primary" PRIMARY KEY("id");
CREATE TABLE "Comment"(
    "id" BIGINT NOT NULL,
    "commenter" BIGINT NOT NULL,
    "post" BIGINT NOT NULL,
    "published_date" DATE NOT NULL,
    "content" TEXT NOT NULL
);
ALTER TABLE
    "Comment" ADD CONSTRAINT "comment_id_primary" PRIMARY KEY("id");
ALTER TABLE
    "Reply" ADD CONSTRAINT "reply_replier_foreign" FOREIGN KEY("replier") REFERENCES "User1"("id");
ALTER TABLE

    "Comment" ADD CONSTRAINT "comment_commenter_foreign" FOREIGN KEY("commenter") REFERENCES "User1"("id");
ALTER TABLE
    "Comment" ADD CONSTRAINT "comment_post_foreign" FOREIGN KEY("post") REFERENCES "Post"("id");
ALTER TABLE
    "Reply" ADD CONSTRAINT "reply_parent_comment_foreign" FOREIGN KEY("parent_comment") REFERENCES "Comment"("id");
ALTER TABLE
    "Post" ADD CONSTRAINT "post_category_foreign" FOREIGN KEY("category") REFERENCES "Category"("id");
ALTER TABLE
    "Post" ADD CONSTRAINT "post_author_foreign" FOREIGN KEY("author") REFERENCES "User1"("id");