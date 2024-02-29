/*
Navicat MySQL Data Transfer
Source Host     : localhost:3306
Source Database : sql
Target Host     : localhost:3306
Target Database : sql
Date: 2023-05-15 11:02:58
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for help_table
-- ----------------------------
DROP TABLE IF EXISTS `help_table`;
CREATE TABLE `help_table` (
  `content` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`content`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of help_table
-- ----------------------------
INSERT INTO `help_table` VALUES ('Question1：如何爬取商品ID？\r\nAnswer：进入系统后，首先点击爬取ID栏目，然后根据提示输入商品网址，最后点击搜索即可得到商品ID。');
INSERT INTO `help_table` VALUES ('Question2：如何爬取商品评论？\r\nAnswer：第一步，爬取商品ID；第二步，点击京东爬虫根据提示输入信息（注意文件名后缀是.csv）；第三步，点击确定即可生成所需的文件。');
INSERT INTO `help_table` VALUES ('Question3：评分筛查功能如何使用？\r\nAnswer：首先输入需要筛选的评论所在的文件名，然后输入评论筛选后导出的文件名（自命名），再选择您需要筛选的分值，最后点击确定即可得到评论筛选后的文件。');
INSERT INTO `help_table` VALUES ('Question4:如何进行数据分析？\r\nAnswer:第一步，从browse查找文件所在的路径并打开；第二步，如果想要生成词频柱状图，首先输入关键词的个数N（例如：10），然后输入词频柱状图文件名（文件名.jpg或文件名.png）最后点击生成词频柱状图按钮即可；第三步，如果想要生成词云，首先输入词云文件名（文件名.jpg或文件名.png），然后点击生成词云按钮即可；第四步，点击进行LDA主题分析。');
INSERT INTO `help_table` VALUES ('Question5：如何查看生成的词云和词频柱状图？\r\nAnswer：以查看生成的词云为例：第一步，点击图片查看功能；第二步：输入想要查看的的词云文件名；第三步，选择正确的后缀名；第四步，点击查看词云即可在当前页面查看生成的词云。查看词频柱状图同理。');

-- ----------------------------
-- Table structure for jingdong_table
-- ----------------------------
DROP TABLE IF EXISTS `jingdong_table`;
CREATE TABLE `jingdong_table` (
  `content` varchar(100) NOT NULL,
  PRIMARY KEY (`content`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of jingdong_table
-- ----------------------------
INSERT INTO `jingdong_table` VALUES ('ID是京东商品的唯一标识，你可以在商品详情页的URL中找到它');
INSERT INTO `jingdong_table` VALUES ('网址l是你要爬取的商品列表页的地址，你可以在京东搜索框中输入关键字，然后根据筛选条件来生成url');

-- ----------------------------
-- Table structure for notice_table
-- ----------------------------
DROP TABLE IF EXISTS `notice_table`;
CREATE TABLE `notice_table` (
  `content` varchar(100) NOT NULL,
  PRIMARY KEY (`content`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of notice_table
-- ----------------------------
INSERT INTO `notice_table` VALUES ('请等待更新通知。。。。。');

-- ----------------------------
-- Table structure for userlogin
-- ----------------------------
DROP TABLE IF EXISTS `userlogin`;
CREATE TABLE `userlogin` (
  `username` varchar(12) NOT NULL,
  `password` int DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of userlogin
-- ----------------------------
INSERT INTO `userlogin` VALUES ('1', '1');
INSERT INTO `userlogin` VALUES ('123', '123');
INSERT INTO `userlogin` VALUES ('1234', '1234');
INSERT INTO `userlogin` VALUES ('512', '512');
INSERT INTO `userlogin` VALUES ('李聪聪', '12345678');
INSERT INTO `userlogin` VALUES ('钢铁侠', '1234');
INSERT INTO `userlogin` VALUES ('阿凡达', '112233');
