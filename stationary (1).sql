-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 08, 2020 at 08:01 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stationary`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `c_id` int(11) NOT NULL,
  `customer_name` varchar(150) NOT NULL,
  `product_detail` varchar(200) NOT NULL,
  `total_amount` double NOT NULL,
  `sent_amount` double DEFAULT NULL,
  `remaining_amount` double DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`c_id`, `customer_name`, `product_detail`, `total_amount`, `sent_amount`, `remaining_amount`, `timestamp`) VALUES
(2, 'faisal pro', 'insaaf q-35', 24000, 0, 0, '2020-09-08 03:23:44'),
(3, 'taha new', 'rekseen 3kg q-30', 12000, 11000, 0, '2020-09-08 04:07:39'),
(4, 'moshin', 'galan q-30', 23000, 2000, 21000, '2020-09-08 04:45:50');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `product_catagory` varchar(150) NOT NULL,
  `quantity` int(11) NOT NULL,
  `purchase_price` double NOT NULL,
  `sales_price` double DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `product_catagory`, `quantity`, `purchase_price`, `sales_price`, `timestamp`) VALUES
(24, 'rekseen', 'brown', 4, 34567, 13629, '2020-08-31 07:17:46'),
(27, 'rekseen', 'silver', 0, 3456, 1293, '2020-08-31 07:22:12'),
(28, 'rekseeen', 'glow', 34, 2345.456, 44400, '2020-08-31 07:24:17'),
(31, 'marker', 'piano', 5, 1400, 4500, '2020-09-01 05:34:45'),
(32, 'rekseen', 'black', 1, 50000, 20220, '2020-09-07 07:13:20');

-- --------------------------------------------------------

--
-- Table structure for table `sales_products`
--

CREATE TABLE `sales_products` (
  `s_product_no` int(11) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `product_catagory` varchar(150) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price_per_product` double NOT NULL,
  `sales_price` double NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sales_products`
--

INSERT INTO `sales_products` (`s_product_no`, `product_name`, `product_catagory`, `quantity`, `price_per_product`, `sales_price`, `date`) VALUES
(47, 'rekseen', 'brown', 5, 2300, 11500, '2020-09-07'),
(48, 'rekseeen', 'glow', 200, 222, 44400, '2020-09-07'),
(49, 'insaaf', 'galan', 200, 200, 5600, '2020-09-06'),
(50, 'insaaf', 'galan', 200, 200, 560, '2020-09-06');

-- --------------------------------------------------------

--
-- Table structure for table `sent_amount`
--

CREATE TABLE `sent_amount` (
  `id` int(11) NOT NULL,
  `customer_name` varchar(150) NOT NULL,
  `product_detail` varchar(200) NOT NULL,
  `s_amount` double NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sent_amount`
--

INSERT INTO `sent_amount` (`id`, `customer_name`, `product_detail`, `s_amount`, `timestamp`) VALUES
(1, 'taha new', 'rekseen 3kg q-30', 1000, '2020-09-08 04:42:17'),
(2, 'moshin', 'galan q-30', 2000, '2020-09-08 04:46:09');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `sales_products`
--
ALTER TABLE `sales_products`
  ADD PRIMARY KEY (`s_product_no`);

--
-- Indexes for table `sent_amount`
--
ALTER TABLE `sent_amount`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `sales_products`
--
ALTER TABLE `sales_products`
  MODIFY `s_product_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `sent_amount`
--
ALTER TABLE `sent_amount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
