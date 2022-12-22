-- 테이블 순서는 관계를 고려하여 한 번에 실행해도 에러가 발생하지 않게 정렬되었습니다.

-- user Table Create SQL
-- 테이블 생성 SQL - user
CREATE TABLE user
(
    `id`             INT            NOT NULL    AUTO_INCREMENT, 
    `name`           VARCHAR(45)    NULL, 
    `password`       TINYTEXT       NULL, 
    `email`          VARCHAR(45)    NULL, 
    `profile_image`  TINYTEXT       NULL, 
     PRIMARY KEY (id)
);


-- video Table Create SQL
-- 테이블 생성 SQL - video
CREATE TABLE video
(
    `id`           INT            NOT NULL    AUTO_INCREMENT, 
    `title`        VARCHAR(45)    NOT NULL, 
    `video_url`    TINYTEXT       NOT NULL, 
    `like`         INT            NOT NULL, 
    `dislike`      INT            NOT NULL, 
    `tag`          VARCHAR(45)    NOT NULL, 
    `uploader_id`  INT            NOT NULL, 
     PRIMARY KEY (id)
);

-- Foreign Key 설정 SQL - video(uploader_id) -> user(id)
ALTER TABLE video
    ADD CONSTRAINT FK_video_uploader_id_user_id FOREIGN KEY (uploader_id)
        REFERENCES user (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Foreign Key 삭제 SQL - video(uploader_id)
-- ALTER TABLE video
-- DROP FOREIGN KEY FK_video_uploader_id_user_id;


-- likes Table Create SQL
-- 테이블 생성 SQL - likes
CREATE TABLE likes
(
    `id`        INT            NOT NULL    AUTO_INCREMENT, 
    `user_id`   INT            NOT NULL, 
    `video_id`  INT            NOT NULL, 
    `type`      VARCHAR(45)    NOT NULL, 
     PRIMARY KEY (id)
);

-- Foreign Key 설정 SQL - likes(user_id) -> user(id)
ALTER TABLE likes
    ADD CONSTRAINT FK_likes_user_id_user_id FOREIGN KEY (user_id)
        REFERENCES user (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Foreign Key 삭제 SQL - likes(user_id)
-- ALTER TABLE likes
-- DROP FOREIGN KEY FK_likes_user_id_user_id;

-- Foreign Key 설정 SQL - likes(video_id) -> video(id)
ALTER TABLE likes
    ADD CONSTRAINT FK_likes_video_id_video_id FOREIGN KEY (video_id)
        REFERENCES video (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Foreign Key 삭제 SQL - likes(video_id)
-- ALTER TABLE likes
-- DROP FOREIGN KEY FK_likes_video_id_video_id;


-- follow Table Create SQL
-- 테이블 생성 SQL - follow
CREATE TABLE follow
(
    `id`         INT    NOT NULL    AUTO_INCREMENT, 
    `user_id`    INT    NOT NULL, 
    `target_id`  INT    NOT NULL, 
     PRIMARY KEY (id)
);

-- Foreign Key 설정 SQL - follow(user_id) -> user(id)
ALTER TABLE follow
    ADD CONSTRAINT FK_follow_user_id_user_id FOREIGN KEY (user_id)
        REFERENCES user (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Foreign Key 삭제 SQL - follow(user_id)
-- ALTER TABLE follow
-- DROP FOREIGN KEY FK_follow_user_id_user_id;

-- Foreign Key 설정 SQL - follow(target_id) -> user(id)
ALTER TABLE follow
    ADD CONSTRAINT FK_follow_target_id_user_id FOREIGN KEY (target_id)
        REFERENCES user (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Foreign Key 삭제 SQL - follow(target_id)
-- ALTER TABLE follow
-- DROP FOREIGN KEY FK_follow_target_id_user_id;


-- comment Table Create SQL
-- 테이블 생성 SQL - comment
CREATE TABLE comment
(
    `id`            INT    NOT NULL    AUTO_INCREMENT, 
    `video_id`      INT    NOT NULL, 
    `commenter_id`  INT    NOT NULL, 
    `content`       INT    NOT NULL, 
    `like`          INT    NOT NULL, 
     PRIMARY KEY (id)
);

-- Foreign Key 설정 SQL - comment(video_id) -> video(id)
ALTER TABLE comment
    ADD CONSTRAINT FK_comment_video_id_video_id FOREIGN KEY (video_id)
        REFERENCES video (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Foreign Key 삭제 SQL - comment(video_id)
-- ALTER TABLE comment
-- DROP FOREIGN KEY FK_comment_video_id_video_id;

-- Foreign Key 설정 SQL - comment(commenter_id) -> user(id)
ALTER TABLE comment
    ADD CONSTRAINT FK_comment_commenter_id_user_id FOREIGN KEY (commenter_id)
        REFERENCES user (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

-- Foreign Key 삭제 SQL - comment(commenter_id)
-- ALTER TABLE comment
-- DROP FOREIGN KEY FK_comment_commenter_id_user_id;




CREATE TABLE reply
(
    `id`            INT    NOT NULL    AUTO_INCREMENT, 
    `comment_id`      INT    NOT NULL, 
    `commenter_id`  INT    NOT NULL, 
    `content`       INT    NOT NULL, 
    `like`          INT    NOT NULL, 
     PRIMARY KEY (id)
);

ALTER TABLE reply
    ADD CONSTRAINT FK_reply_comment_id_comment_id FOREIGN KEY (comment_id)
        REFERENCES comment (id) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE reply
    ADD CONSTRAINT FK_reply_commenter_id_user_id FOREIGN KEY (commenter_id)
        REFERENCES user (id) ON DELETE RESTRICT ON UPDATE RESTRICT;