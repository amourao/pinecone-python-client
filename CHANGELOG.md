# Changelog

## Unreleased Changes

## [2.0.7](https://github.com/pinecone-io/pinecone-python-client/compare/v2.0.7...v2.0.6) - 2022-03-01

### Changed
- Increased maximum length of ids to 512

## [2.0.6](https://github.com/pinecone-io/pinecone-python-client/compare/v2.0.6...v2.0.5) - 2022-02-15

### Changed
- Changed the spec to add  ```pods``` and ```pod_type``` fields to ```create_index``` and ```describe_index```.
- ```pod_type``` is used to select between ```'s1'``` and ```'p1'``` pod types during index creation.
- The field ```pods``` means total number of pods the index will use, ```pods = shards*replicas```.

## [2.0.5](https://github.com/pinecone-io/pinecone-python-client/compare/v2.0.5...v2.0.4) - 2022-01-17

### Changed

- Increased the max vector dimensionality to 20k.

## [2.0.4](https://github.com/pinecone-io/pinecone-python-client/compare/v2.0.4...v2.0.3) - 2021-12-20

### Changed

- Public release of the gRPC flavor of client. The gRPC flavor comes with more dependencies but can give higher upsert speeds on multi node indexes. For more details on the gRPC client, please refer to the [installation](https://www.pinecone.io/docs/installation/) and [usage](https://www.pinecone.io/docs/performance-tuning/#using-the-grpc-client-to-get-higher-upsert-speeds) sections in the docs.
## [2.0.3](https://github.com/pinecone-io/pinecone-python-client/compare/v2.0.3...v2.0.2) - 2021-10-31

### Changed

- Some type validations were moved to the backend for performance reasons. In these cases a 4xx ApiException will be returned instead of an ApiTypeError.

## [2.0.2] - 2021-10-21

### Changed
- The python client `pinecone.config.OpenApiConfiguration` object now uses the certifi package's SSL CA bundle by default. This should fix HTTPS connection errors in certain environments depending on their default CA bundle, including some Google Colab notebooks. 
- A bug causing different index instances to share the same configuration object was fixed.
- Deprecated control via `pinecone.init()` of the pinecone logger's log level and removed the loguru dependency. To control log level now, use the standard library's logging module to manage the level of the "pinecone" logger or its children. 


## [2.0.1] - 2021-10-06
### Added
- New `timeout` parameter to the `pinecone.create_index()` and the `pinecone.delete_index()` call.
  - `timeout` allows you to set how many seconds you want to wait for `create_index()` and `delete_index()` to complete. If `None`, wait indefinitely; if `>=0`, time out after this many seconds; if `-1`, return immediately and do not wait. Defaults to `None`.

### Changed
- Updates the default openapi_config object to use the certifice ssl_ca_cert bundle.
- The python client `pinecone.config.OpenApiConfiguration` object now uses the certifi package's SSL CA bundle by default. This should fix HTTPS connection errors in certain environments depending on their default CA bundle, including some Google Colab notebooks. 

## 2.0.0 - 2020-10-04
### Added
- New major release!

### Changed
- `pinecone.create_index()` now requires a `dimension` parameter.
- The `pinecone.Index` interface has changed:
  - `Index.upsert`, `Index.query`, `Index.fetch`, and `Index.delete` now take different parameters and return different results.
  - `Index.info` has been removed. See `Index.describe_index_stats()` as an alternative.
  - The `Index()` constructor no longer validates index existence. This is instead done on all operations executed using the Index instance.

[2.0.2]: https://github.com/pinecone-io/pinecone-python-client/compare/v2.0.1...v2.0.2
[2.0.1]: https://github.com/pinecone-io/pinecone-python-client/compare/v2.0.0...v2.0.1
