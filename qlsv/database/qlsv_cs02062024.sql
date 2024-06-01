-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th6 02, 2024 lúc 01:45 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlsv_cs`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app_thongtinphongbgh_bangiamhieu`
--

CREATE TABLE `app_thongtinphongbgh_bangiamhieu` (
  `MNV` varchar(15) NOT NULL,
  `Hoten` varchar(50) NOT NULL,
  `Ngaysinh` date DEFAULT NULL,
  `Gioitinh` int(11) NOT NULL,
  `SDT` varchar(12) DEFAULT NULL,
  `Email` varchar(254) DEFAULT NULL,
  `Roles` int(11) NOT NULL,
  `Matkhau` varchar(50) NOT NULL,
  `Image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `app_thongtinphongbgh_bangiamhieu`
--

INSERT INTO `app_thongtinphongbgh_bangiamhieu` (`MNV`, `Hoten`, `Ngaysinh`, `Gioitinh`, `SDT`, `Email`, `Roles`, `Matkhau`, `Image`) VALUES
('HT0001', 'PGS.TS Phan Cao Thọ', '1963-09-05', 0, '0846875275', 'pct@ute.udn.vn', 1, 'PCT-UTE_@@', 'avt/24/phan_cao_tho_vAqfWzr.jpg');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app_thongtinphongctsv_phongctsv`
--

CREATE TABLE `app_thongtinphongctsv_phongctsv` (
  `MNV` varchar(15) NOT NULL,
  `Hoten` varchar(50) NOT NULL,
  `Ngaysinh` date DEFAULT NULL,
  `Gioitinh` int(11) NOT NULL,
  `SDT` varchar(12) DEFAULT NULL,
  `Email` varchar(254) DEFAULT NULL,
  `Roles` int(11) NOT NULL,
  `Matkhau` varchar(50) NOT NULL,
  `Image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `app_thongtinphongctsv_phongctsv`
--

INSERT INTO `app_thongtinphongctsv_phongctsv` (`MNV`, `Hoten`, `Ngaysinh`, `Gioitinh`, `SDT`, `Email`, `Roles`, `Matkhau`, `Image`) VALUES
('CTSV001', 'Nguyễn Tấn Hòa', '1975-07-05', 0, '0914030651', 'nthoa@ute.udn.vn', 0, 'CTSV-NTH@', 'avt/24/phan_cao_tho_m3hdTzs.jpg');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `app_thongtinsinhvien_sinhvien`
--

CREATE TABLE `app_thongtinsinhvien_sinhvien` (
  `MSV` varchar(15) NOT NULL,
  `Hoten` varchar(50) NOT NULL,
  `Ngaysinh` date NOT NULL,
  `Gioitinh` int(11) NOT NULL,
  `CCCD` varchar(12) NOT NULL,
  `Quequan` varchar(255) NOT NULL,
  `SDT` varchar(12) NOT NULL,
  `Email` varchar(254) NOT NULL,
  `Lopsinhhoat` varchar(10) NOT NULL,
  `Nganhhoc` varchar(50) NOT NULL,
  `Khoa` varchar(50) NOT NULL,
  `Nienkhoa` varchar(9) NOT NULL,
  `Dantoc` varchar(255) NOT NULL,
  `Matkhau` varchar(50) NOT NULL,
  `Image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `app_thongtinsinhvien_sinhvien`
--

INSERT INTO `app_thongtinsinhvien_sinhvien` (`MSV`, `Hoten`, `Ngaysinh`, `Gioitinh`, `CCCD`, `Quequan`, `SDT`, `Email`, `Lopsinhhoat`, `Nganhhoc`, `Khoa`, `Nienkhoa`, `Dantoc`, `Matkhau`, `Image`) VALUES
('21115053120138', 'La Thế Quyền', '2003-07-02', 0, '066203002013', 'EaNam - EaHleo - Đắk Lắk', '0867089934', 'thequyenla@gmail.com', '21T1', 'Công nghệ thông tin', 'Công nghệ số', '2021', 'Kinh', '12345@', 'avt/24/quyenne.jpg'),
('21115053120200', 'Hồ Bá Đông', '2003-05-22', 0, '066203002000', 'Hải Châu - Đà Nẵng', '0357384934', 'donghoba@gmail.com', '21T1', 'Công nghệ thông tin', 'Công nghệ số', '2021', 'Kinh', '12345@', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add sinh vien', 7, 'add_sinhvien'),
(26, 'Can change sinh vien', 7, 'change_sinhvien'),
(27, 'Can delete sinh vien', 7, 'delete_sinhvien'),
(28, 'Can view sinh vien', 7, 'view_sinhvien'),
(29, 'Can add dai dien phong ban', 8, 'add_daidienphongban'),
(30, 'Can change dai dien phong ban', 8, 'change_daidienphongban'),
(31, 'Can delete dai dien phong ban', 8, 'delete_daidienphongban'),
(32, 'Can view dai dien phong ban', 8, 'view_daidienphongban'),
(33, 'Can add dai dien phong ban', 9, 'add_daidienphongban'),
(34, 'Can change dai dien phong ban', 9, 'change_daidienphongban'),
(35, 'Can delete dai dien phong ban', 9, 'delete_daidienphongban'),
(36, 'Can view dai dien phong ban', 9, 'view_daidienphongban'),
(37, 'Can add dai dien phong ban', 10, 'add_daidienphongban'),
(38, 'Can change dai dien phong ban', 10, 'change_daidienphongban'),
(39, 'Can delete dai dien phong ban', 10, 'delete_daidienphongban'),
(40, 'Can view dai dien phong ban', 10, 'view_daidienphongban'),
(41, 'Can add dai dien phong ban', 11, 'add_daidienphongban'),
(42, 'Can change dai dien phong ban', 11, 'change_daidienphongban'),
(43, 'Can delete dai dien phong ban', 11, 'delete_daidienphongban'),
(44, 'Can view dai dien phong ban', 11, 'view_daidienphongban'),
(45, 'Can add phong ctsv', 10, 'add_phongctsv'),
(46, 'Can change phong ctsv', 10, 'change_phongctsv'),
(47, 'Can delete phong ctsv', 10, 'delete_phongctsv'),
(48, 'Can view phong ctsv', 10, 'view_phongctsv'),
(49, 'Can add ban giam hieu', 11, 'add_bangiamhieu'),
(50, 'Can change ban giam hieu', 11, 'change_bangiamhieu'),
(51, 'Can delete ban giam hieu', 11, 'delete_bangiamhieu'),
(52, 'Can view ban giam hieu', 11, 'view_bangiamhieu');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$3Su0dnsorg13lNtEGD6gN2$SK0HA1WLkWTncWRm5WNQ+GJGiypf1+0l0qOm9M52SPU=', '2024-06-01 20:29:55.596124', 1, 'lathequyen', '', '', 'quyenlathe4@gmail.com', 1, 1, '2024-05-21 19:58:41.114729');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-05-21 20:08:00.089554', '21115053120138', '21115053120138', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-05-22 09:01:14.670345', '21115053120200', '21115053120200', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-05-22 21:41:53.573012', '21115053120138', '21115053120138', 2, '[]', 7, 1),
(4, '2024-05-29 03:36:49.902881', 'CTSV001', 'CTSV001', 1, '[{\"added\": {}}]', 8, 1),
(5, '2024-05-29 04:46:30.196918', 'CTSV001', 'CTSV001', 1, '[{\"added\": {}}]', 8, 1),
(6, '2024-05-29 05:19:17.184751', 'CTSV001', 'CTSV001', 1, '[{\"added\": {}}]', 9, 1),
(7, '2024-05-31 05:23:06.512268', '21115053120138', '[21115053120138] - La Thế Quyền', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(8, '2024-05-31 05:23:14.153912', '21115053120138', '[21115053120138] - La Thế Quyền', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(9, '2024-05-31 05:41:01.135414', '21115053120138', '[21115053120138] - La Thế Quyền', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(10, '2024-05-31 05:59:04.847657', '21115053120138', '[21115053120138] - La Thế Quyền', 2, '[{\"changed\": {\"fields\": [\"Matkhau\", \"Image\"]}}]', 7, 1),
(11, '2024-05-31 06:03:16.622950', '21115053120138', '[21115053120138] - La Thế Quyền', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(12, '2024-05-31 06:30:31.433619', '21115053120138', '[21115053120138] - La Thế Quyền', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(13, '2024-05-31 07:00:54.522541', '21115053120138', '[21115053120138] - La Thế Quyền', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(14, '2024-05-31 23:01:36.546742', '0001', '[0001] - Nguyễn Tấn Hòa', 1, '[{\"added\": {}}]', 10, 1),
(15, '2024-05-31 23:02:53.972875', '0001', '[0001] - Nguyễn Quang Thọ', 1, '[{\"added\": {}}]', 11, 1),
(16, '2024-05-31 23:12:14.777542', '0001', '[0001] - Nguyễn Tấn Hòa', 2, '[]', 10, 1),
(17, '2024-05-31 23:12:44.969452', '0001', '[0001] - Nguyễn Tấn Hòa', 3, '', 10, 1),
(18, '2024-05-31 23:13:05.284943', 'CTSV001', '[CTSV001] - Nguyễn Tấn Hòa', 1, '[{\"added\": {}}]', 10, 1),
(19, '2024-05-31 23:13:50.242116', 'CTSV002', '[CTSV002] - Nguyễn Tấn Hòa', 1, '[{\"added\": {}}]', 10, 1),
(20, '2024-06-01 21:38:00.357215', '0001', '[0001] - Nguyễn Quang Thọ', 3, '', 11, 1),
(21, '2024-06-01 21:43:03.127819', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 1, '[{\"added\": {}}]', 11, 1),
(22, '2024-06-01 21:54:45.244018', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 2, '[{\"changed\": {\"fields\": [\"Roles\"]}}]', 11, 1),
(23, '2024-06-01 22:05:47.263141', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 2, '[{\"changed\": {\"fields\": [\"Roles\"]}}]', 11, 1),
(24, '2024-06-01 22:07:43.734388', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 2, '[{\"changed\": {\"fields\": [\"Roles\"]}}]', 11, 1),
(25, '2024-06-01 22:12:58.904182', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 2, '[]', 11, 1),
(26, '2024-06-01 22:13:01.697273', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 2, '[]', 11, 1),
(27, '2024-06-01 22:37:57.081625', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 1, '[{\"added\": {}}]', 11, 1),
(28, '2024-06-01 22:41:47.178065', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 3, '', 11, 1),
(29, '2024-06-01 23:07:04.065024', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 1, '[{\"added\": {}}]', 11, 1),
(30, '2024-06-01 23:07:09.283564', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 2, '[]', 11, 1),
(31, '2024-06-01 23:11:18.310495', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 3, '', 11, 1),
(32, '2024-06-01 23:12:35.566078', 'HT0001', '[HT0001] - gfjfgjgfjg', 1, '[{\"added\": {}}]', 11, 1),
(33, '2024-06-01 23:25:37.893662', 'HT0001', '[HT0001] - PGS.TS Phan Cao Thọ', 2, '[{\"changed\": {\"fields\": [\"Hoten\", \"SDT\", \"Email\", \"Matkhau\", \"Image\"]}}]', 11, 1),
(34, '2024-06-01 23:30:17.561362', 'CTSV002', '[CTSV002] - Nguyễn Tấn Hòa', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 10, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(11, 'app_thongtinphongBGH', 'bangiamhieu'),
(10, 'app_thongtinphongCTSV', 'phongctsv'),
(7, 'app_thongtinsinhvien', 'sinhvien'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-21 02:51:50.919123'),
(2, 'auth', '0001_initial', '2024-05-21 02:51:51.452931'),
(3, 'admin', '0001_initial', '2024-05-21 02:51:51.578308'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-05-21 02:51:51.585482'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-21 02:51:51.594941'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-05-21 02:51:51.657546'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-05-21 02:51:51.716299'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-05-21 02:51:51.731215'),
(9, 'auth', '0004_alter_user_username_opts', '2024-05-21 02:51:51.738758'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-05-21 02:51:51.789666'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-05-21 02:51:51.792670'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-21 02:51:51.799986'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-05-21 02:51:51.815511'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-21 02:51:51.829887'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-05-21 02:51:51.844851'),
(16, 'auth', '0011_update_proxy_permissions', '2024-05-21 02:51:51.853737'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-21 02:51:51.868546'),
(18, 'sessions', '0001_initial', '2024-05-21 02:51:51.915757'),
(19, 'app_thongtinsinhvien', '0001_initial', '2024-05-21 19:04:00.803121'),
(20, 'app_thongtinsinhvien', '0002_alter_sinhvien_gioitinh', '2024-05-22 21:39:34.192832'),
(21, 'app_thongtinsinhvien', '0003_alter_sinhvien_gioitinh', '2024-05-29 02:17:31.983026'),
(22, 'app_thongtinsinhvien', '0004_rename_pass_sinhvien_matkhau', '2024-05-29 02:17:32.010582'),
(23, 'app_thongtinPCTSV', '0001_initial', '2024-05-29 03:18:52.506277'),
(24, 'app_thongtinPCTSV', '0002_rename_pass_daidienphongban_matkhau', '2024-05-29 03:45:37.462929'),
(25, 'app_thongtinphongban', '0001_initial', '2024-05-29 05:17:54.366333'),
(26, 'app_thongtinsinhvien', '0005_sinhvien_image_alter_sinhvien_email', '2024-05-31 04:38:18.549802'),
(27, 'app_thongtinsinhvien', '0006_alter_sinhvien_image', '2024-05-31 06:23:28.519622'),
(28, 'app_thongtinsinhvien', '0007_alter_sinhvien_email_alter_sinhvien_sdt', '2024-05-31 06:25:41.019600'),
(29, 'app_thongtinsinhvien', '0008_alter_sinhvien_image', '2024-05-31 06:29:25.576590'),
(30, 'app_thongtinsinhvien', '0009_alter_sinhvien_image', '2024-05-31 06:58:32.663621'),
(31, 'app_thongtinsinhvien', '0010_alter_sinhvien_image', '2024-05-31 21:54:31.005876'),
(32, 'app_thongtinphongBGH', '0001_initial', '2024-05-31 22:47:34.229558'),
(33, 'app_thongtinphongBGH', '0002_daidienphongban_image_alter_daidienphongban_roles', '2024-05-31 22:47:34.249254'),
(34, 'app_thongtinphongCTSV', '0001_initial', '2024-05-31 22:47:34.260988'),
(35, 'app_thongtinphongCTSV', '0002_remove_daidienphongban_unique_hieu_truong_and_more', '2024-05-31 22:47:34.281789'),
(36, 'app_thongtinsinhvien', '0011_alter_sinhvien_image', '2024-05-31 22:47:34.290244'),
(37, 'app_thongtinphongBGH', '0003_rename_daidienphongban_bangiamhieu', '2024-05-31 22:57:45.032091'),
(38, 'app_thongtinphongCTSV', '0003_rename_daidienphongban_phongctsv', '2024-05-31 22:57:45.064051'),
(39, 'app_thongtinphongBGH', '0004_alter_bangiamhieu_email_alter_bangiamhieu_sdt', '2024-05-31 23:00:19.796414'),
(40, 'app_thongtinphongCTSV', '0004_alter_phongctsv_email_alter_phongctsv_sdt', '2024-05-31 23:00:19.819152'),
(41, 'app_thongtinphongBGH', '0005_alter_bangiamhieu_matkhau', '2024-06-01 22:20:26.310590'),
(42, 'app_thongtinphongBGH', '0006_alter_bangiamhieu_matkhau', '2024-06-01 22:36:23.603119'),
(43, 'app_thongtinphongBGH', '0007_alter_bangiamhieu_matkhau', '2024-06-01 22:36:23.605422'),
(44, 'app_thongtinphongBGH', '0008_alter_bangiamhieu_matkhau', '2024-06-01 22:36:23.613470'),
(45, 'app_thongtinphongBGH', '0009_alter_bangiamhieu_email_alter_bangiamhieu_gioitinh_and_more', '2024-06-01 22:41:07.853800'),
(46, 'app_thongtinphongBGH', '0002_alter_bangiamhieu_email_alter_bangiamhieu_image_and_more', '2024-06-01 23:06:46.248954'),
(47, 'app_thongtinphongCTSV', '0005_alter_phongctsv_email_alter_phongctsv_gioitinh_and_more', '2024-06-01 23:29:43.847652');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2033gq19t3kc6omu9g7mykwcpd41fqvc', '.eJxVjMsOwiAQRf-FtSHQ8nBcuvcbyMwAUjWQlHZl_HdD0oVu7znnvkXAfSth72kNSxQXocXpdyPkZ6oDxAfWe5Pc6rYuJIciD9rlrcX0uh7u30HBXkYNPOPENoNDilqzYZ_BGMicQUfFGV08g1KKnNaEXhEpazDbafbJgfh8AQU0OFk:1sDVMR:eF3kwO8suc_7csqLM_pt4fbpPcA2AdQHJ7M7AOswzIg', '2024-06-15 20:29:55.597047'),
('nmsaty1qqesz5etbjg9v7qym4wy5zmih', '.eJxVjMsOwiAQRf-FtSHQ8nBcuvcbyMwAUjWQlHZl_HdD0oVu7znnvkXAfSth72kNSxQXocXpdyPkZ6oDxAfWe5Pc6rYuJIciD9rlrcX0uh7u30HBXkYNPOPENoNDilqzYZ_BGMicQUfFGV08g1KKnNaEXhEpazDbafbJgfh8AQU0OFk:1s9VdM:Xy02YfvI11-pK14q-Xd3eptlJn_CB0rciczWnfVJQJA', '2024-06-04 19:58:52.053939');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `app_thongtinphongctsv_phongctsv`
--
ALTER TABLE `app_thongtinphongctsv_phongctsv`
  ADD PRIMARY KEY (`MNV`);

--
-- Chỉ mục cho bảng `app_thongtinsinhvien_sinhvien`
--
ALTER TABLE `app_thongtinsinhvien_sinhvien`
  ADD PRIMARY KEY (`MSV`),
  ADD UNIQUE KEY `app_thongtinsinhvien_sinhvien_Email_5dd6eabf_uniq` (`Email`);

--
-- Chỉ mục cho bảng `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Chỉ mục cho bảng `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Chỉ mục cho bảng `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Chỉ mục cho bảng `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Chỉ mục cho bảng `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Chỉ mục cho bảng `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Chỉ mục cho bảng `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Chỉ mục cho bảng `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Chỉ mục cho bảng `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT cho bảng `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT cho bảng `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT cho bảng `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Các ràng buộc cho bảng `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
