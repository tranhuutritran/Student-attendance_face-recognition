-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2022 at 03:34 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diemdanhsv`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_ten` varchar(10) NOT NULL,
  `admin_matkhau` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_ten`, `admin_matkhau`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `buoihoc`
--

CREATE TABLE `buoihoc` (
  `buoihoc_id` int(10) NOT NULL,
  `buoihoc_giobatdau` time DEFAULT NULL,
  `buoihoc_gioketthuc` time DEFAULT NULL,
  `buoihoc_ngay` date NOT NULL,
  `giangvien_id` int(4) NOT NULL,
  `monhoc_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buoihoc`
--

INSERT INTO `buoihoc` (`buoihoc_id`, `buoihoc_giobatdau`, `buoihoc_gioketthuc`, `buoihoc_ngay`, `giangvien_id`, `monhoc_id`) VALUES
(1, '09:00:00', '11:00:00', '2022-12-01', 1806, 'CT332'),
(2, '09:20:00', '11:30:00', '2022-12-01', 1806, 'CT332'),
(3, '09:00:00', '11:00:00', '2022-12-01', 2524, 'CT175'),
(4, '09:30:00', '11:30:00', '2022-12-01', 2524, 'CT175'),
(5, '10:00:00', '11:30:00', '2022-12-01', 2524, 'CT112H01'),
(6, '08:50:00', '10:30:00', '2022-12-01', 1806, 'CT332'),
(7, '09:30:00', '11:30:00', '2022-12-01', 2524, 'CT112H01'),
(8, '09:30:00', '11:30:00', '2022-12-01', 2524, 'CT175'),
(9, '10:00:00', '12:30:00', '2022-12-01', 1806, 'CT332'),
(10, '10:00:00', '11:30:00', '2022-12-01', 2524, 'CT112H01');

-- --------------------------------------------------------

--
-- Table structure for table `diemdanh`
--

CREATE TABLE `diemdanh` (
  `diemdanh_id` varchar(32) NOT NULL,
  `sinhvien_id` int(7) DEFAULT NULL,
  `diemdanh_giovao` time DEFAULT NULL,
  `diemdanh_giora` time DEFAULT NULL,
  `diemdanh_ngay` date DEFAULT NULL,
  `buoihoc_id` int(10) DEFAULT NULL,
  `diemdanh_trangthai` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `diemdanh`
--

INSERT INTO `diemdanh` (`diemdanh_id`, `sinhvien_id`, `diemdanh_giovao`, `diemdanh_giora`, `diemdanh_ngay`, `buoihoc_id`, `diemdanh_trangthai`) VALUES

('SV1812809202212013', 1812809, '09:23:16', '11:12:00', '2022-12-01', 3, 'Đi muộn 23 phút'),
('SV1809599202212014', 1809599, '09:23:43', '11:18:23', '2022-12-01', 4, 'Có mặt'),
('SV1809599202212015', 1809599, '09:24:03', '11:26:12', '2022-12-01', 5, 'Có mặt'),
('SV1809599202212016', 1809599, '09:24:41', '10:32:54', '2022-12-01', 6, 'Đi muộn 34 phút'),
('SV1809599202212017', 1809599, '09:25:03', '11:20:19', '2022-12-01', 7, 'Có mặt'),
('SV1910257202212012', 1910257, '09:22:40', '11:45:39', '2022-12-01', 2, 'Đi muộn 2 phút');

-- --------------------------------------------------------

--
-- Table structure for table `giangvien`
--

CREATE TABLE `giangvien` (
  `giangvien_id` int(4) NOT NULL,
  `giangvien_ten` varchar(32) NOT NULL,
  `giangvien_sdt` varchar(10) NOT NULL,
  `giangvien_email` varchar(32) NOT NULL,
  `giangvien_cauhoi` varchar(32) NOT NULL,
  `giangvien_traloi` varchar(45) NOT NULL,
  `giangvien_matkhau` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `giangvien`
--

INSERT INTO `giangvien` (`giangvien_id`, `giangvien_ten`, `giangvien_sdt`, `giangvien_email`, `giangvien_cauhoi`, `giangvien_traloi`, `giangvien_matkhau`) VALUES
(1806, 'Sử Kim Anh', '0916377006', 'skanh@ctu.edu.vn', 'Bạn thích ăn gì', 'code', '12345'),
(2326, 'Nguyễn Văn Nay', '0123456789', 'nvnay@ctu.edu.vn', 'Chữ số bạn thích', '1111', '12345'),
(2378, 'Nguyễn Hoàng Anh', '0919577004', 'hoanganh@ctu.edu.vn', 'Chữ số bạn thích', '10', '12345'),
(2459, 'Trần Duy Phát', '0123456789', 'tdphat@ctu.edu.vn', 'Bạn thích ăn gì', 'bánh mì', '12345'),
(2477, 'Nguyễn Thiết', '0123456789', 'nthiet@ctu.edu.vn', 'Chữ số bạn thích', '9999', '12345'),
(2509, 'Lê Trần Thanh Liêm', '0902537483', 'lttliem@ctu.edu.vn', 'Chữ số bạn thích', '100', '12345'),
(2524, 'Nguyễn Tí Hon', '0989641121', 'nthon@ctu.edu.vn', 'Sở thích của bạn', 'code', '12345'),
(2525, 'Cao Quốc Nam', '0123456789', 'cqnam@ctu.edu.vn', 'Sở thích của bạn', 'du lịch', '12345'),
(2625, 'Võ Hồng Dũng', '0123446789', 'vhdung@ctu.edu.vn', 'Sở thích của bạn', 'học ngoại ngữ', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `lop`
--

CREATE TABLE `lop` (
  `lop_id` varchar(32) NOT NULL,
  `lop_ten` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `lop`
--

INSERT INTO `lop` (`lop_id`, `lop_ten`) VALUES
('HG18T7', 'Kỹ thuật xây dựng'),
('HG18U7A1', 'Kinh doanh nông nghiệp A1'),
('HG18U7A2', 'Kinh doanh nông nghiệp A2'),
('HG18V7A1', 'Công nghệ thông tin A1'),
('HG18V7A2', 'Công nghệ thông tin A2'),
('HG18W8', 'Việt Nam học');

-- --------------------------------------------------------

--
-- Table structure for table `monhoc`
--

CREATE TABLE `monhoc` (
  `monhoc_id` varchar(8) NOT NULL,
  `monhoc_ten` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `monhoc`
--

INSERT INTO `monhoc` (`monhoc_id`, `monhoc_ten`) VALUES
('CT112H01', 'Mạng máy tính'),
('CT112H02', 'Mạng máy tính'),
('CT175', 'Lý thuyết đồ thị'),
('CT180', 'Cơ sở dữ liệu'),
('CT202H01', 'Nguyên lý máy học'),
('CT202H02', 'Nguyên lý máy học'),
('CT221', 'An ninh mạng'),
('CT222', 'An toàn hệ thống'),
('CT332', 'Trí tuệ nhân tạo'),
('KT103', 'Quản trị học'),
('KT106', 'Nguyên lý kế toán'),
('KT113H01', 'Kinh tế lượng'),
('KT113H02', 'Kinh tế lượng'),
('KT316', 'Kinh doanh quốc tế'),
('XH137', 'Dân số và phát triển'),
('XH190', 'Y tế du lịch'),
('XH409', 'Du lịch văn hóa'),
('XH426', 'Phát triển du lịch bền vững');

-- --------------------------------------------------------

--
-- Table structure for table `monhocgiangvien`
--

CREATE TABLE `monhocgiangvien` (
  `giangvien_id` int(4) NOT NULL,
  `monhoc_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `monhocgiangvien`
--

INSERT INTO `monhocgiangvien` (`giangvien_id`, `monhoc_id`) VALUES
(1806, 'CT112H02'),
(1806, 'CT332'),
(2459, 'XH409'),
(2509, 'KT103'),
(2524, 'CT112H01'),
(2524, 'CT175'),
(2525, 'KT113H01'),
(2625, 'XH137');

-- --------------------------------------------------------

--
-- Table structure for table `monhocsinhvien`
--

CREATE TABLE `monhocsinhvien` (
  `sinhvien_id` int(7) NOT NULL,
  `monhoc_id` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `monhocsinhvien`
--

INSERT INTO `monhocsinhvien` (`sinhvien_id`, `monhoc_id`) VALUES
(1809599, 'CT112H01'),
(1809599, 'CT175'),
(1809599, 'CT332'),
(1809601, 'CT175'),
(1809601, 'CT332'),
(1809609, 'CT332'),
(1809622, 'CT175'),
(1809632, 'CT332'),
(1809661, 'CT112H01'),
(1809661, 'CT175'),
(1809661, 'CT332'),
(1812809, 'CT112H01'),
(1812809, 'CT175'),
(1812815, 'CT112H01'),
(1812815, 'CT332'),
(1812820, 'CT112H01'),
(1812820, 'CT175'),
(1812820, 'CT332'),
(1910257, 'CT112H01'),
(1910257, 'CT175'),
(1910257, 'CT332');

-- --------------------------------------------------------

--
-- Table structure for table `sinhvien`
--

CREATE TABLE `sinhvien` (
  `sinhvien_id` int(7) NOT NULL,
  `sinhvien_namhoc` varchar(32) DEFAULT NULL,
  `sinhvien_hocky` varchar(32) DEFAULT NULL,
  `sinhvien_ten` varchar(32) DEFAULT NULL,
  `lop_id` varchar(32) NOT NULL,
  `sinhvien_gioitinh` varchar(10) DEFAULT NULL,
  `sinhvien_ngaysinh` date DEFAULT NULL,
  `sinhvien_email` varchar(32) DEFAULT NULL,
  `sinhvien_hinh` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sinhvien`
--

INSERT INTO `sinhvien` (`sinhvien_id`, `sinhvien_namhoc`, `sinhvien_hocky`, `sinhvien_ten`, `lop_id`, `sinhvien_gioitinh`, `sinhvien_ngaysinh`, `sinhvien_email`, `sinhvien_hinh`) VALUES
(1806423, '2022-23', 'Học kì I', 'Thái Trung Nhựt', 'HG18U7A1', 'Nam', '2000-03-09', 'nhutb1806423@student.ctu.edu.vn', 'Yes'),
(1806817, '2022-23', 'Học kì I', 'Trần Phước Long', 'HG18V7A2', 'Nam', '2000-12-04', 'longb1806817@student.ctu.edu.vn', 'No'),
(1809572, '2022-23', 'Học kì I', 'Lâm Văn Hào', 'HG18V7A2', 'Nam', '2000-07-09', 'haob1809572@student.ctu.edu.vn', 'No'),
(1809594, '2022-23', 'Học kì I', 'Võ Đình Khôi', 'HG18V7A2', 'Nam', '2000-03-07', 'khoib1809594@student.ctu.edu.vn', 'No'),
(1809599, '2022-23', 'Học kì I', 'Nguyễn Nguyên Linh', 'HG18V7A1', 'Nam', '2000-11-09', 'linhb1809599@student.ctu.edu.vn', 'No'),
(1809601, '2022-23', 'Học kì I', 'Phạm Thị Linh', 'HG18V7A1', 'Nữ', '2000-08-27', 'linhb1809601@student.ctu.edu.vn', 'No'),
(1809605, '2022-23', 'Học kì I', 'Lê Công Lý', 'HG18V7A1', 'Nam', '2000-04-10', 'lyb1809605@student.ctu.edu.vn', 'No'),
(1809608, '2022-23', 'Học kì I', 'Nguyễn Thị Kiều My', 'HG18V7A1', 'Nữ', '2000-11-24', 'myb1809608@student.ctu.edu.vn', 'No'),
(1809609, '2022-23', 'Học kì I', 'Nguyễn Hoài Nam', 'HG18V7A1', 'Nam', '2000-09-15', 'namb1809609@student.ctu.edu.vn', 'No'),
(1809622, '2022-23', 'Học kì I', 'Trần Dương Nhất', 'HG18V7A1', 'Nam', '2000-03-22', 'nhatb1809661@student.ctu.edu.vn', 'Yes'),
(1809632, '2022-23', 'Học kì I', 'Nguyễn Thanh Phong', 'HG18V7A2', 'Nam', '2000-12-09', 'phongb1809632@student.ctu.edu.vn', 'Yes'),
(1809634, '2022-23', 'Học kì I', 'Lê Ánh Phượng', 'HG18V7A1', 'Nữ', '2000-04-15', 'phuongb1809634@student.ctu.edu.v', 'No'),
(1809658, '2022-23', 'Học kì I', 'Trương Quốc Triệu', 'HG18V7A1', 'Nam', '2000-04-18', 'trieub1809658@student.ctu.edu', 'Yes'),
(1809661, '2022-23', 'Học kì I', 'Trần Hữu Trí', 'HG18V7A1', 'Nam', '0000-00-00', 'trib1809661@student.ctu.edu.vn', 'Yes'),
(1812241, '2022-23', 'Học kì I', 'Trần Văn Thi', 'HG18T7', 'Nam', '2022-11-11', 'thib1812241@student.ctu.edu.vn', 'Yes'),
(1812809, '2022-23', 'Học kì I', 'Võ Thị Ngọc Nữ', 'HG18V7A2', 'Nữ', '2000-02-23', 'nub1812809@student.ctu.edu.vn', 'No'),
(1812815, '2022-23', 'Học kì I', 'Trần Đức Thiện', 'HG18V7A2', 'Nam', '2000-06-22', 'thienb1812815@student.ctu.edu.vn', 'No'),
(1812820, '2022-23', 'Học kì I', 'Nguyễn Văn Tốt', 'HG18V7A1', 'Nam', '2000-08-29', 'totb1812820@student.ctu.edu.vn', 'No'),
(1910257, '2022-23', 'Học kì I', 'Châu Quang Minh', 'HG18V7A1', 'Nam', '0000-00-00', 'minhb1910257@student.ctu.edu.vn', 'No');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_ten`);

--
-- Indexes for table `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD PRIMARY KEY (`buoihoc_id`),
  ADD KEY `Teacher_id` (`giangvien_id`),
  ADD KEY `Subject_id` (`monhoc_id`);

--
-- Indexes for table `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD PRIMARY KEY (`diemdanh_id`),
  ADD KEY `Lesson_id` (`buoihoc_id`),
  ADD KEY `Student_id` (`sinhvien_id`);

--
-- Indexes for table `giangvien`
--
ALTER TABLE `giangvien`
  ADD PRIMARY KEY (`giangvien_id`);

--
-- Indexes for table `lop`
--
ALTER TABLE `lop`
  ADD PRIMARY KEY (`lop_id`);

--
-- Indexes for table `monhoc`
--
ALTER TABLE `monhoc`
  ADD PRIMARY KEY (`monhoc_id`);

--
-- Indexes for table `monhocgiangvien`
--
ALTER TABLE `monhocgiangvien`
  ADD PRIMARY KEY (`giangvien_id`,`monhoc_id`),
  ADD KEY `Teacher_id` (`giangvien_id`),
  ADD KEY `Subject_id` (`monhoc_id`);

--
-- Indexes for table `monhocsinhvien`
--
ALTER TABLE `monhocsinhvien`
  ADD PRIMARY KEY (`sinhvien_id`,`monhoc_id`),
  ADD KEY `Student_id` (`sinhvien_id`),
  ADD KEY `Subject_id` (`monhoc_id`);

--
-- Indexes for table `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD PRIMARY KEY (`sinhvien_id`),
  ADD KEY `Class` (`lop_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `buoihoc`
--
ALTER TABLE `buoihoc`
  ADD CONSTRAINT `buoihoc_ibfk_3` FOREIGN KEY (`monhoc_id`) REFERENCES `monhoc` (`monhoc_id`),
  ADD CONSTRAINT `buoihoc_ibfk_4` FOREIGN KEY (`giangvien_id`) REFERENCES `giangvien` (`giangvien_id`);

--
-- Constraints for table `diemdanh`
--
ALTER TABLE `diemdanh`
  ADD CONSTRAINT `diemdanh_ibfk_3` FOREIGN KEY (`sinhvien_id`) REFERENCES `sinhvien` (`sinhvien_id`),
  ADD CONSTRAINT `diemdanh_ibfk_4` FOREIGN KEY (`buoihoc_id`) REFERENCES `buoihoc` (`buoihoc_id`);

--
-- Constraints for table `monhocgiangvien`
--
ALTER TABLE `monhocgiangvien`
  ADD CONSTRAINT `monhocgiangvien_ibfk_1` FOREIGN KEY (`monhoc_id`) REFERENCES `monhoc` (`monhoc_id`),
  ADD CONSTRAINT `monhocgiangvien_ibfk_2` FOREIGN KEY (`giangvien_id`) REFERENCES `giangvien` (`giangvien_id`);

--
-- Constraints for table `monhocsinhvien`
--
ALTER TABLE `monhocsinhvien`
  ADD CONSTRAINT `monhocsinhvien_ibfk_1` FOREIGN KEY (`sinhvien_id`) REFERENCES `sinhvien` (`sinhvien_id`),
  ADD CONSTRAINT `monhocsinhvien_ibfk_2` FOREIGN KEY (`monhoc_id`) REFERENCES `monhoc` (`monhoc_id`);

--
-- Constraints for table `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD CONSTRAINT `sinhvien_ibfk_1` FOREIGN KEY (`lop_id`) REFERENCES `lop` (`lop_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
