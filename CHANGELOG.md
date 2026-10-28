# Changelog

## [0.31.0](https://github.com/meteroid-oss/meteroid-python/compare/v0.30.1...v0.31.0) (2026-10-28)


### ⚠ BREAKING CHANGES

* **api:** update SDKs to meteroid 0.1.0 ([#15](https://github.com/meteroid-oss/meteroid-python/issues/15))
* **api:** `GET /api/v1/coupons`: added `#/components/schemas/CreditDiscount` to the `data/items/discount` response property `oneOf` list for the response status `200`
* **api:** `GET /api/v1/coupons/{coupon_id}`: added `#/components/schemas/CreditDiscount` to the `discount` response property `oneOf` list for the response status `200`
* **api:** `GET /api/v1/plans`: added `#/components/schemas/CreditPlanFee` to the `data/items/price_components/items/fee/oneOf[#/components/schemas/Fee]/` response property `oneOf` list for the response status `200`
* **api:** `GET /api/v1/plans/{plan_id}`: added `#/components/schemas/CreditPlanFee` to the `price_components/items/fee/oneOf[#/components/schemas/Fee]/` response property `oneOf` list for the response status `200`
* **api:** `GET /api/v1/products`: added `#/components/schemas/CreditFeeStructure` to the `data/items/fee_structure` response property `oneOf` list for the response status `200`
* **api:** `GET /api/v1/products/{product_id}`: added `#/components/schemas/CreditFeeStructure` to the `fee_structure` response property `oneOf` list for the response status `200`
* **api:** `GET /api/v1/subscriptions/{subscription_id}`: added `#/components/schemas/CreditDiscount` to the `applied_coupons/items/coupon/discount` response property `oneOf` list for the response status `200`
* **api:** `GET /api/v1/subscriptions/{subscription_id}`: added `#/components/schemas/CreditFee` to the `add_ons/items/fee` response property `oneOf` list for the response status `200`
* **api:** `GET /api/v1/subscriptions/{subscription_id}`: added `#/components/schemas/CreditFee` to the `components/items/fee` response property `oneOf` list for the response status `200`
* **api:** `PATCH /api/v1/coupons/{coupon_id}`: added the new required request property `discount/oneOf[#/components/schemas/CouponDiscount]/oneOf[#/components/schemas/FixedDiscount]/type`
* **api:** 90 more breaking changes

### Features

* **api:** `GET /api/v1/coupons/{coupon_id}`: added `#/components/schemas/CreditDiscount` to the `discount` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `GET /api/v1/coupons`: added `#/components/schemas/CreditDiscount` to the `data/items/discount` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `GET /api/v1/plans/{plan_id}`: added `#/components/schemas/CreditPlanFee` to the `price_components/items/fee/oneOf[#/components/schemas/Fee]/` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `GET /api/v1/plans`: added `#/components/schemas/CreditPlanFee` to the `data/items/price_components/items/fee/oneOf[#/components/schemas/Fee]/` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `GET /api/v1/products/{product_id}`: added `#/components/schemas/CreditFeeStructure` to the `fee_structure` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `GET /api/v1/products`: added `#/components/schemas/CreditFeeStructure` to the `data/items/fee_structure` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `GET /api/v1/subscriptions/{subscription_id}`: added `#/components/schemas/CreditDiscount` to the `applied_coupons/items/coupon/discount` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `GET /api/v1/subscriptions/{subscription_id}`: added `#/components/schemas/CreditFee` to the `add_ons/items/fee` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `GET /api/v1/subscriptions/{subscription_id}`: added `#/components/schemas/CreditFee` to the `components/items/fee` response property `oneOf` list for the response status `200` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** `PATCH /api/v1/coupons/{coupon_id}`: added the new required request property `discount/oneOf[#/components/schemas/CouponDiscount]/oneOf[#/components/schemas/FixedDiscount]/type` ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** 90 more breaking changes ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** update SDKs to meteroid 0.1.0 ([#15](https://github.com/meteroid-oss/meteroid-python/issues/15)) ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))
* **api:** update the API definitions ([338794d](https://github.com/meteroid-oss/meteroid-python/commit/338794d71dd156584ae3e8880eeef7bac6eaf86c))

## [0.30.1](https://github.com/meteroid-oss/meteroid-python/compare/v0.30.0...v0.30.1) (2026-10-16)


### Bug Fixes

* **api:** update SDKs to meteroid 0.1.0 ([#13](https://github.com/meteroid-oss/meteroid-python/issues/13)) ([6d51785](https://github.com/meteroid-oss/meteroid-python/commit/6d51785f3244058ef028de4366dd440ceb37fced))

## [0.30.0](https://github.com/meteroid-oss/meteroid-python/compare/v0.29.0...v0.30.0) (2026-10-09)


### ⚠ BREAKING CHANGES

* **api:** update SDKs to meteroid 0.1.0 ([#11](https://github.com/meteroid-oss/meteroid-python/issues/11))
* **api:** `POST /api/v1/events/ingest`: the `events/items/timestamp` request property `type/format` changed from `string` to `string, null/date-time`

### Features

* **api:** `POST /api/v1/events/ingest`: the `events/items/timestamp` request property `type/format` changed from `string` to `string, null/date-time` ([39cacd4](https://github.com/meteroid-oss/meteroid-python/commit/39cacd4d911d35f9ee8b579007bea7be344b07ce))
* **api:** add `DELETE /api/v1/webhooks/endpoints/{endpoint_id}` ([39cacd4](https://github.com/meteroid-oss/meteroid-python/commit/39cacd4d911d35f9ee8b579007bea7be344b07ce))
* **api:** update `GET /api/v1/plans` and 1029 more ([39cacd4](https://github.com/meteroid-oss/meteroid-python/commit/39cacd4d911d35f9ee8b579007bea7be344b07ce))
* **api:** update SDKs to meteroid 0.1.0 ([#11](https://github.com/meteroid-oss/meteroid-python/issues/11)) ([39cacd4](https://github.com/meteroid-oss/meteroid-python/commit/39cacd4d911d35f9ee8b579007bea7be344b07ce))

## [0.29.0](https://github.com/meteroid-oss/meteroid-python/compare/v0.28.0...v0.29.0) (2026-10-08)


### ⚠ BREAKING CHANGES

* **api:** update SDKs to meteroid 0.1.0 ([#9](https://github.com/meteroid-oss/meteroid-python/issues/9))

### Features

* **api:** update SDKs to meteroid 0.1.0 ([#9](https://github.com/meteroid-oss/meteroid-python/issues/9)) ([080c5bc](https://github.com/meteroid-oss/meteroid-python/commit/080c5bce1b19845064da84396a6181fd1d0036f5))

## [0.28.0](https://github.com/meteroid-oss/meteroid-python/compare/v0.27.1...v0.28.0) (2026-10-07)


### ⚠ BREAKING CHANGES

* **api:** update SDKs to meteroid 0.1.0 ([#8](https://github.com/meteroid-oss/meteroid-python/issues/8))

### Features

* **api:** update SDKs to meteroid 0.1.0 ([#8](https://github.com/meteroid-oss/meteroid-python/issues/8)) ([6263e19](https://github.com/meteroid-oss/meteroid-python/commit/6263e19f302acf0810964b4e07c9228719bfa6f5))


### Documentation

* describe the SDK and link to Meteroid ([#5](https://github.com/meteroid-oss/meteroid-python/issues/5)) ([3d31c15](https://github.com/meteroid-oss/meteroid-python/commit/3d31c159c5c8bb4920f18022374dbe40a578a373))
* document pagination and the default base URL ([#7](https://github.com/meteroid-oss/meteroid-python/issues/7)) ([bb3e257](https://github.com/meteroid-oss/meteroid-python/commit/bb3e2576c4cd3674f6b8008a5857c66c0af90641))

## [0.27.1](https://github.com/meteroid-oss/meteroid-python/compare/v0.27.0...v0.27.1) (2026-10-06)


### Bug Fixes

* **api:** update SDKs to meteroid 0.1.0 ([#3](https://github.com/meteroid-oss/meteroid-python/issues/3)) ([00121b9](https://github.com/meteroid-oss/meteroid-python/commit/00121b967f53b75036daa165fa13fff2f8f4bb22))

## [0.27.0](https://github.com/meteroid-oss/meteroid-python/compare/v0.1.0...v0.27.0) (2026-10-06)


### Features

* **api:** update SDKs to meteroid 0.1.0 ([#1](https://github.com/meteroid-oss/meteroid-python/issues/1)) ([5ae24a5](https://github.com/meteroid-oss/meteroid-python/commit/5ae24a5dd692a7f3ba1a162ab795bab088541122))
