CREATE TABLE `backtest_record` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `started_at` timestamp DEFAULT NULL,
  `stopped_at` timestamp DEFAULT NULL,
  `strategy_class` varchar(255) NOT NULL,
  `strategy_params` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_strategy_class_started_at` (`strategy_class`, `started_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `backtest_fill` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `record_id` bigint(20) NOT NULL,
  `symbol` varchar(255) NOT NULL,
  `traded_qty` float NOT NULL,
  `traded_price` float NOT NULL,
  `traded_at` timestamp NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_record_id_symbol` (`record_id`, `symbol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
