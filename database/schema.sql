-- This file contains table definitions for the database.


DROP TABLE input_date CASCADE;
DROP TABLE trigger CASCADE;
DROP TABLE sleep_rating CASCADE;
DROP TABLE water_rating CASCADE;
DROP TABLE meal_rating CASCADE;
DROP TABLE exercise_rating CASCADE;
DROP TABLE stress_rating CASCADE;
DROP TABLE lonely_rating CASCADE;
DROP TABLE mental_rating CASCADE;
DROP TABLE happiness_rating CASCADE;
DROP TABLE emotion CASCADE;
DROP TABLE user CASCADE;
DROP TABLE user_trigger CASCADE;
DROP TABLE user_wellbeing CASCADE;
DROP TABLE user_mental_health CASCADE;
DROP TABLE user_emotion CASCADE;


CREATE TABLE input_date (
    input_date_id INT GENERATED ALWAYS AS IDENTITY,
    input_date DATE NOT NULL,
    PRIMARY KEY (input_date_id)
);


CREATE TABLE trigger (
    trigger_id INT GENERATED ALWAYS AS IDENTITY,
    trigger_name VARCHAR(20) UNIQUE NOT NULL,
    PRIMARY KEY (trigger_id)
);


CREATE TABLE sleep_rating (
    sleep_rating_id INT GENERATED ALWAYS AS IDENTITY,
    sleep_rating INT NOT NULL,
    PRIMARY KEY (sleep_rating_id)
);


CREATE TABLE water_rating (
    water_rating_id INT GENERATED ALWAYS AS IDENTITY,
    water_rating INT NOT NULL,
    PRIMARY KEY (water_rating_id)
);


CREATE TABLE meal_rating (
    meal_rating_id INT GENERATED ALWAYS AS IDENTITY,
    meal_rating INT NOT NULL,
    PRIMARY KEY (meal_rating_id)
);


CREATE TABLE exercise_rating (
    exercise_rating_id INT GENERATED ALWAYS AS IDENTITY,
    exercise_rating INT NOT NULL,
    PRIMARY KEY (exercise_rating_id)
);


CREATE TABLE stress_rating (
    stress_rating_id INT GENERATED ALWAYS AS IDENTITY,
    stress_rating INT NOT NULL,
    PRIMARY KEY (stress_rating_id)
);


CREATE TABLE lonely_rating (
    lonely_rating_id INT GENERATED ALWAYS AS IDENTITY,
    lonely_rating INT NOT NULL,
    PRIMARY KEY (lonely_rating_id)
);


CREATE TABLE mental_rating (
    mental_rating_id INT GENERATED ALWAYS AS IDENTITY,
    mental_rating INT NOT NULL,
    PRIMARY KEY (mental_rating_id)
);


CREATE TABLE happiness_rating (
    happiness_rating_id INT GENERATED ALWAYS AS IDENTITY,
    happiness_rating INT NOT NULL,
    PRIMARY KEY (happiness_rating_id)
);


CREATE TABLE emotion (
    emotion_id INT GENERATED ALWAYS AS IDENTITY,
    emotion_name VARCHAR(20) UNIQUE NOT NULL,
    PRIMARY KEY (emotion_id)
);


CREATE TABLE user (
    user_id INT GENERATED ALWAYS AS IDENTITY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    PRIMARY KEY (user_id)
);


CREATE TABLE user_trigger (
    user_trigger_id INT GENERATED ALWAYS AS IDENTITY,
    trigger_id INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (user_trigger_id),
    FOREIGN KEY(trigger_id) REFERENCES trigger(trigger_id),
    FOREIGN KEY(user_id) REFERENCES user(user_id)
);


CREATE TABLE user_wellbeing (
    user_wellbeing_id INT GENERATED ALWAYS AS IDENTITY,
    user_id INT NOT NULL,
    input_date_id DATE NOT NULL,
    sleep_rating_id INT,
    water_rating_id INT,
    meal_rating_id INT,
    exercise_rating_id INT,
    PRIMARY KEY (user_wellbeing_id),
    FOREIGN KEY(user_id) REFERENCES user(user_id),
    FOREIGN KEY(input_date_id) REFERENCES input_date(input_date_id),
    FOREIGN KEY(sleep_rating_id) REFERENCES sleep_rating(sleep_rating_id),
    FOREIGN KEY(water_rating_id) REFERENCES water_rating(water_rating_id),
    FOREIGN KEY(meal_rating_id) REFERENCES meal_rating(meal_rating_id),
    FOREIGN KEY(exercise_rating_id) REFERENCES exercise_rating(exercise_rating_id)
);


CREATE TABLE user_mental_health (
    user_mental_id INT GENERATED ALWAYS AS IDENTITY,
    user_id INT NOT NULL,
    input_date_id DATE NOT NULL,
    stress_rating_id INT,
    lonely_rating_id INT,
    mental_rating_id INT NOT NULL,
    happiness_rating_id INT NOT NULL,
    services_awareness BOOLEAN NOT NULL,
    need_to_talk BOOLEAN NOT NULL,
    PRIMARY KEY (user_mental_id),
    FOREIGN KEY(user_id) REFERENCES user(user_id),
    FOREIGN KEY(input_date_id) REFERENCES input_date(input_date_id),
    FOREIGN KEY(stress_rating_id) REFERENCES stress_rating(stress_rating_id),
    FOREIGN KEY(lonely_rating_id) REFERENCES lonely_rating(lonely_rating_id),
    FOREIGN KEY(mental_rating_id) REFERENCES mental_rating(mental_rating_id),
    FOREIGN KEY(happiness_rating_id) REFERENCES happiness_rating(happiness_rating_id)
);


CREATE TABLE user_emotion (
    user_emotion_id INT GENERATED ALWAYS AS IDENTITY,
    user_id INT NOT NULL,
    input_date_id DATE NOT NULL,
    emotion_id INT NOT NULL,
    PRIMARY KEY (user_emotion_id),
    FOREIGN KEY(user_id) REFERENCES user(user_id),
    FOREIGN KEY(input_date_id) REFERENCES input_date(input_date_id),
    FOREIGN KEY(emotion_id) REFERENCES emotion(emotion_id)
);