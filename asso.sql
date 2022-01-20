-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Jan 20, 2022 at 08:46 AM
-- Server version: 5.7.24
-- PHP Version: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `asso`
--

-- --------------------------------------------------------

--
-- Table structure for table `donnateurs`
--

CREATE TABLE `donnateurs` (
  `id_donnateur` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telephone` int(12) NOT NULL,
  `don_fin` int(250) DEFAULT NULL,
  `don_tps` varchar(250) NOT NULL,
  `don_mat` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `donnateurs`
--

INSERT INTO `donnateurs` (`id_donnateur`, `nom`, `prenom`, `email`, `telephone`, `don_fin`, `don_tps`, `don_mat`) VALUES
(5, 'Jacques', 'Jean', 'JeanJ@gmail.com', 299876578, 45, '', ''),
(6, 'Perez', 'Francisco', 'frpe@gmail.com', 212556677, NULL, 'Garder un animal en détresse à votre domicile', ''),
(7, 'Hollande', 'Francois', 'frholl@gmail.com', 121334472, 1850, '', ''),
(8, 'Sarkozy', 'Nicolas', 'ns@gmail.com', 101010101, 2, '', ''),
(9, 'Chirac', 'Jacques', 'jaco@elysee.fr', 181212812, 48, 'Rien', 'Rien'),
(10, 'Poutou', 'Philippe', 'fifi@orange.com', 654667798, 0, 'Rien', 'Panier ou autre couchage'),
(11, 'Taubira', 'Christiane', 'chrichri@pink.fr', 125678854, 400, 'Faire des rondes avec notre groupe pour repérer les abus', 'Rien'),
(12, 'Chazal', 'Claire', 'cc@tf1.fr', 167289201, 0, 'Rien', 'Boîtes de pâtée chiot');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `donnateurs`
--
ALTER TABLE `donnateurs`
  ADD PRIMARY KEY (`id_donnateur`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `donnateurs`
--
ALTER TABLE `donnateurs`
  MODIFY `id_donnateur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
