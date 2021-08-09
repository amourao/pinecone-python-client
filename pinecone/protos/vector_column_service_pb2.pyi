# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from typing import (
    Iterable as typing___Iterable,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class NdArray(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    buffer: builtin___bytes = ...
    shape: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    dtype: typing___Text = ...
    compressed: builtin___bool = ...

    def __init__(self,
        *,
        buffer : typing___Optional[builtin___bytes] = None,
        shape : typing___Optional[typing___Iterable[builtin___int]] = None,
        dtype : typing___Optional[typing___Text] = None,
        compressed : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"buffer",b"buffer",u"compressed",b"compressed",u"dtype",b"dtype",u"shape",b"shape"]) -> None: ...
type___NdArray = NdArray

class Status(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    StatusCodeValue = typing___NewType('StatusCodeValue', builtin___int)
    type___StatusCodeValue = StatusCodeValue
    StatusCode: _StatusCode
    class _StatusCode(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[Status.StatusCodeValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        SUCCESS = typing___cast(Status.StatusCodeValue, 0)
        READY = typing___cast(Status.StatusCodeValue, 1)
        ERROR = typing___cast(Status.StatusCodeValue, 2)
        ERROR_DUPLICATE = typing___cast(Status.StatusCodeValue, 3)
    SUCCESS = typing___cast(Status.StatusCodeValue, 0)
    READY = typing___cast(Status.StatusCodeValue, 1)
    ERROR = typing___cast(Status.StatusCodeValue, 2)
    ERROR_DUPLICATE = typing___cast(Status.StatusCodeValue, 3)
    type___StatusCode = StatusCode

    class Details(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        function: typing___Text = ...
        function_id: typing___Text = ...
        exception: typing___Text = ...
        traceback: typing___Text = ...

        @property
        def time(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

        def __init__(self,
            *,
            function : typing___Optional[typing___Text] = None,
            function_id : typing___Optional[typing___Text] = None,
            exception : typing___Optional[typing___Text] = None,
            traceback : typing___Optional[typing___Text] = None,
            time : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"time",b"time"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"exception",b"exception",u"function",b"function",u"function_id",b"function_id",u"time",b"time",u"traceback",b"traceback"]) -> None: ...
    type___Details = Details

    class AvgTimeEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: builtin___int = ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[builtin___int] = None,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...
    type___AvgTimeEntry = AvgTimeEntry

    code: type___Status.StatusCodeValue = ...
    description: typing___Text = ...
    msg_sent: builtin___int = ...
    msg_recv: builtin___int = ...
    size: builtin___int = ...

    @property
    def details(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___Status.Details]: ...

    @property
    def avg_time(self) -> typing___MutableMapping[typing___Text, builtin___int]: ...

    def __init__(self,
        *,
        code : typing___Optional[type___Status.StatusCodeValue] = None,
        description : typing___Optional[typing___Text] = None,
        details : typing___Optional[typing___Iterable[type___Status.Details]] = None,
        msg_sent : typing___Optional[builtin___int] = None,
        msg_recv : typing___Optional[builtin___int] = None,
        avg_time : typing___Optional[typing___Mapping[typing___Text, builtin___int]] = None,
        size : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"avg_time",b"avg_time",u"code",b"code",u"description",b"description",u"details",b"details",u"msg_recv",b"msg_recv",u"msg_sent",b"msg_sent",u"size",b"size"]) -> None: ...
type___Status = Status

class ScoredResults(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def ids(self) -> type___NdArray: ...

    @property
    def scores(self) -> type___NdArray: ...

    @property
    def data(self) -> type___NdArray: ...

    @property
    def metadata(self) -> type___NdArray: ...

    def __init__(self,
        *,
        ids : typing___Optional[type___NdArray] = None,
        scores : typing___Optional[type___NdArray] = None,
        data : typing___Optional[type___NdArray] = None,
        metadata : typing___Optional[type___NdArray] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data",u"ids",b"ids",u"metadata",b"metadata",u"scores",b"scores"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"ids",b"ids",u"metadata",b"metadata",u"scores",b"scores"]) -> None: ...
type___ScoredResults = ScoredResults

class UpsertRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    metadata: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    @property
    def data(self) -> type___NdArray: ...

    def __init__(self,
        *,
        namespace : typing___Optional[typing___Text] = None,
        ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        data : typing___Optional[type___NdArray] = None,
        metadata : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"ids",b"ids",u"metadata",b"metadata",u"namespace",b"namespace"]) -> None: ...
type___UpsertRequest = UpsertRequest

class UpsertResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___UpsertResponse = UpsertResponse

class DeleteRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    delete_all: builtin___bool = ...

    def __init__(self,
        *,
        namespace : typing___Optional[typing___Text] = None,
        ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        delete_all : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"delete_all",b"delete_all",u"ids",b"ids",u"namespace",b"namespace"]) -> None: ...
type___DeleteRequest = DeleteRequest

class DeleteResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___DeleteResponse = DeleteResponse

class FetchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    def __init__(self,
        *,
        namespace : typing___Optional[typing___Text] = None,
        ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ids",b"ids",u"namespace",b"namespace"]) -> None: ...
type___FetchRequest = FetchRequest

class FetchResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    metadata: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    @property
    def vectors(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___NdArray]: ...

    def __init__(self,
        *,
        namespace : typing___Optional[typing___Text] = None,
        ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        vectors : typing___Optional[typing___Iterable[type___NdArray]] = None,
        metadata : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ids",b"ids",u"metadata",b"metadata",u"namespace",b"namespace",u"vectors",b"vectors"]) -> None: ...
type___FetchResponse = FetchResponse

class QueryRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...
    namespace_overrides: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    top_k: builtin___int = ...
    top_k_overrides: google___protobuf___internal___containers___RepeatedScalarFieldContainer[builtin___int] = ...
    filter: typing___Text = ...
    filter_overrides: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    include_data: builtin___bool = ...
    include_metadata: builtin___bool = ...

    @property
    def queries(self) -> type___NdArray: ...

    def __init__(self,
        *,
        namespace : typing___Optional[typing___Text] = None,
        namespace_overrides : typing___Optional[typing___Iterable[typing___Text]] = None,
        top_k : typing___Optional[builtin___int] = None,
        top_k_overrides : typing___Optional[typing___Iterable[builtin___int]] = None,
        filter : typing___Optional[typing___Text] = None,
        filter_overrides : typing___Optional[typing___Iterable[typing___Text]] = None,
        include_data : typing___Optional[builtin___bool] = None,
        include_metadata : typing___Optional[builtin___bool] = None,
        queries : typing___Optional[type___NdArray] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"queries",b"queries"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"filter",b"filter",u"filter_overrides",b"filter_overrides",u"include_data",b"include_data",u"include_metadata",b"include_metadata",u"namespace",b"namespace",u"namespace_overrides",b"namespace_overrides",u"queries",b"queries",u"top_k",b"top_k",u"top_k_overrides",b"top_k_overrides"]) -> None: ...
type___QueryRequest = QueryRequest

class QueryResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def matches(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___ScoredResults]: ...

    def __init__(self,
        *,
        matches : typing___Optional[typing___Iterable[type___ScoredResults]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"matches",b"matches"]) -> None: ...
type___QueryResponse = QueryResponse

class ListRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...

    def __init__(self,
        *,
        namespace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"namespace",b"namespace"]) -> None: ...
type___ListRequest = ListRequest

class ListResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespace: typing___Text = ...

    @property
    def ids(self) -> type___NdArray: ...

    def __init__(self,
        *,
        ids : typing___Optional[type___NdArray] = None,
        namespace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"ids",b"ids"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ids",b"ids",u"namespace",b"namespace"]) -> None: ...
type___ListResponse = ListResponse

class ListNamespacesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___ListNamespacesRequest = ListNamespacesRequest

class ListNamespacesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespaces: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    def __init__(self,
        *,
        namespaces : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"namespaces",b"namespaces"]) -> None: ...
type___ListNamespacesResponse = ListNamespacesResponse

class SummarizeRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
type___SummarizeRequest = SummarizeRequest

class SummarizeResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    index_size: builtin___int = ...
    dimension: builtin___int = ...

    def __init__(self,
        *,
        index_size : typing___Optional[builtin___int] = None,
        dimension : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dimension",b"dimension",u"index_size",b"index_size"]) -> None: ...
type___SummarizeResponse = SummarizeResponse
