/*
Navicat SQLite Data Transfer

Source Server         : log1
Source Server Version : 30714
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30714
File Encoding         : 65001

Date: 2021-06-13 14:55:27
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for log
-- ----------------------------
DROP TABLE IF EXISTS "main"."log";
CREATE TABLE "log" (
"id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"app_count"  INTEGER,
"uid"  INTEGER,
"app_name"  TEXT(50),
"time"  TEXT(20),
"log_level"  INTEGER,
"log_info"  TEXT(1024),
"create_date"  TimeStamp(20) NOT NULL DEFAULT (datetime('now','localtime'))
);

-- ----------------------------
-- Records of log
-- ----------------------------

-- ----------------------------
-- Table structure for machine
-- ----------------------------
DROP TABLE IF EXISTS "main"."machine";
CREATE TABLE "machine" (
"id"  INTEGER NOT NULL,
"machine"  TEXT,
"machine_info"  TEXT,
"username"  TEXT,
PRIMARY KEY ("id")
);

-- ----------------------------
-- Records of machine
-- ----------------------------

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "main"."sqlite_sequence";
CREATE TABLE sqlite_sequence(name,seq);

-- ----------------------------
-- Records of sqlite_sequence
-- ----------------------------
INSERT INTO "main"."sqlite_sequence" VALUES ('user', 2);
INSERT INTO "main"."sqlite_sequence" VALUES ('log', 0);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "main"."user";
CREATE TABLE "user" (
"id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"username"  TEXT,
"password"  TEXT,
"app_count"  INTEGER DEFAULT 0
);

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO "main"."user" VALUES (1, 'test', 'test', 0);
