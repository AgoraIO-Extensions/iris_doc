import fs.memoryfs
import unittest
from iris_doc.api_tagger import ApiTagger, TagBuilder
from iris_doc.oc.api_tagger_oc import ObjCTagBuilder
input_output_pairs_desc = [
    "Basic Class", "Enums", "class interfaces and complex method params",
    "Protocols", "Class import, interface properties", "Interface methods with no params, and multi params"
]
input_output_pairs = [
("""@interface AgoraRtcEngineKit
- (int)enableDualStreamMode:(BOOL)enabled
    streamConfig:(AgoraSimulcastStreamConfig* _Nonnull)streamConfig NS_SWIFT_NAME(enableDualStreamMode(_:streamConfig:));
@end""","""/* class_agorartcenginekit */
@interface AgoraRtcEngineKit
/* api_agorartcenginekit_enabledualstreammode##streamconfig */
- (int)enableDualStreamMode:(BOOL)enabled
    streamConfig:(AgoraSimulcastStreamConfig* _Nonnull)streamConfig NS_SWIFT_NAME(enableDualStreamMode(_:streamConfig:));
@end"""),
("""/** Audience latency levels in broadcaster mode. */
typedef NS_ENUM(NSInteger, AgoraAudienceLatencyLevelType) {
    /** 1: Low latency. A low latency audience's jitter buffer is 1.2 second. */
    AgoraAudienceLatencyLevelLowLatency = 1,
    /** 2: Default Ultra low latency. An ultra low latency audience's jitter buffer is 0.5 second. */
    AgoraAudienceLatencyLevelUltraLowLatency = 2,
};""","""/* enum_agoraaudiencelatencyleveltype */
typedef NS_ENUM(NSInteger, AgoraAudienceLatencyLevelType) {
/* enum_agoraaudiencelatencyleveltype_agoraaudiencelatencylevellowlatency */
    AgoraAudienceLatencyLevelLowLatency = 1,
/* enum_agoraaudiencelatencyleveltype_agoraaudiencelatencylevelultralowlatency */
    AgoraAudienceLatencyLevelUltraLowLatency = 2,
};"""),
("""NS_ASSUME_NONNULL_BEGIN
@interface AgoraRtcEngineKit(Ex)
- (int)joinChannelExByToken:(NSString* _Nullable)token
                 connection:(AgoraRtcConnection * _Nonnull)connection
                   delegate:(id<AgoraRtcEngineDelegate> _Nullable)delegate
               mediaOptions:(AgoraRtcChannelMediaOptions* _Nonnull)mediaOptions
                joinSuccess:(void(^ _Nullable)(NSString* _Nonnull channel, NSUInteger uid, NSInteger elapsed))joinSuccessBlock NS_SWIFT_NAME(joinChannelEx(byToken:connection:delegate:mediaOptions:joinSuccess:));
@end""", """/* extension_agorartcenginekitex */
NS_ASSUME_NONNULL_BEGIN
@interface AgoraRtcEngineKit(Ex)
/* api_agorartcenginekitex_joinchannelexbytoken##token#connection#delegate#mediaoptions#joinsuccessblock */
- (int)joinChannelExByToken:(NSString* _Nullable)token
                 connection:(AgoraRtcConnection * _Nonnull)connection
                   delegate:(id<AgoraRtcEngineDelegate> _Nullable)delegate
               mediaOptions:(AgoraRtcChannelMediaOptions* _Nonnull)mediaOptions
                joinSuccess:(void(^ _Nullable)(NSString* _Nonnull channel, NSUInteger uid, NSInteger elapsed))joinSuccessBlock NS_SWIFT_NAME(joinChannelEx(byToken:connection:delegate:mediaOptions:joinSuccess:));
@end"""),
("""NS_ASSUME_NONNULL_BEGIN
@protocol AgoraRtcMediaPlayerProtocol <NSObject>
- (int)getMediaPlayerId NS_SWIFT_NAME(getMediaPlayerId());
/**
 * Opens a media file with a specified URL.
 * @param url The URL of the media file that you want to play.
 * @return
 * - 0: Success.
 * - < 0: Failure.
 */
- (int)open:(NSString *)url startPos:(NSInteger)startPos NS_SWIFT_NAME(open(_:startPos:));
@end""", """/* class_agorartcmediaplayerprotocol */
NS_ASSUME_NONNULL_BEGIN
@protocol AgoraRtcMediaPlayerProtocol <NSObject>
/* api_agorartcmediaplayerprotocol_getmediaplayerid */
- (int)getMediaPlayerId NS_SWIFT_NAME(getMediaPlayerId());
/* api_agorartcmediaplayerprotocol_open##url#startpos */
- (int)open:(NSString *)url startPos:(NSInteger)startPos NS_SWIFT_NAME(open(_:startPos:));
@end"""),
("""@class AgoraRtcEngineKit;
__attribute__((visibility("default"))) @interface AgoraMusicContentCenterConfig : NSObject
@property(assign, nonatomic) AgoraRtcEngineKit* _Nullable rtcEngine;
/**
 * The app ID of the project that has enabled the music content center
 */
@property (nonatomic, copy) NSString *appId;
/**
 * The max number which the music content center caches cannot exceed 50.
 */
@property (nonatomic, assign) NSUInteger maxCacheSize;
@end""", """@class AgoraRtcEngineKit;
/* class_agoramusiccontentcenterconfig */
__attribute__((visibility("default"))) @interface AgoraMusicContentCenterConfig : NSObject
/* class_agoramusiccontentcenterconfig_rtcengine */
@property(assign, nonatomic) AgoraRtcEngineKit* _Nullable rtcEngine;
/* class_agoramusiccontentcenterconfig_appid */
@property (nonatomic, copy) NSString *appId;
/* class_agoramusiccontentcenterconfig_maxcachesize */
@property (nonatomic, assign) NSUInteger maxCacheSize;
@end"""),
("""/**
*  hello
*/
__attribute__((visibility("default"))) @interface AgoraLocalSpatialAudioKit : AgoraBaseSpatialAudioKit
+ (instancetype _Nonnull)sharedLocalSpatialAudioWithConfig:(AgoraLocalSpatialAudioConfig* _Nonnull)config NS_SWIFT_NAME(sharedLocalSpatialAudio(with:));
+ (void)destroy NS_SWIFT_NAME(destroy());
- (int)updateRemotePositionEx:(NSUInteger)uid positionInfo:(AgoraRemoteVoicePositionInfo* _Nonnull)posInfo connection:(AgoraRtcConnection * _Nonnull)connection NS_SWIFT_NAME(updateRemotePositionEx(_:positionInfo:connection:));
- (int)removeRemotePosition:(NSUInteger)uid NS_SWIFT_NAME(removeRemotePosition(_:));
- (int)setRemoteAudioAttenuation:(double)attenuation userId:(NSUInteger)uid forceSet:(BOOL)forceSet NS_SWIFT_NAME(setRemoteAudioAttenuation(_:userId:forceSet:));
@end""", """/* class_agoralocalspatialaudiokit */
__attribute__((visibility("default"))) @interface AgoraLocalSpatialAudioKit : AgoraBaseSpatialAudioKit
/* api_agoralocalspatialaudiokit_sharedlocalspatialaudiowithconfig##config */
+ (instancetype _Nonnull)sharedLocalSpatialAudioWithConfig:(AgoraLocalSpatialAudioConfig* _Nonnull)config NS_SWIFT_NAME(sharedLocalSpatialAudio(with:));
/* api_agoralocalspatialaudiokit_destroy */
+ (void)destroy NS_SWIFT_NAME(destroy());
/* api_agoralocalspatialaudiokit_updateremotepositionex##uid#posinfo#connection */
- (int)updateRemotePositionEx:(NSUInteger)uid positionInfo:(AgoraRemoteVoicePositionInfo* _Nonnull)posInfo connection:(AgoraRtcConnection * _Nonnull)connection NS_SWIFT_NAME(updateRemotePositionEx(_:positionInfo:connection:));
/* api_agoralocalspatialaudiokit_removeremoteposition##uid */
- (int)removeRemotePosition:(NSUInteger)uid NS_SWIFT_NAME(removeRemotePosition(_:));
/* api_agoralocalspatialaudiokit_setremoteaudioattenuation##attenuation#uid#forceset */
- (int)setRemoteAudioAttenuation:(double)attenuation userId:(NSUInteger)uid forceSet:(BOOL)forceSet NS_SWIFT_NAME(setRemoteAudioAttenuation(_:userId:forceSet:));
@end""")
]

class TestApiTaggerOc(unittest.TestCase):

    __fileSystem: fs.memoryfs.MemoryFS
    __apiTagger: ApiTagger

    @classmethod
    def setUpClass(self):
        self.__fileSystem = fs.memoryfs.MemoryFS()
        self.__apiTagger = ApiTagger(
            self.__fileSystem, ObjCTagBuilder())

    @classmethod
    def tearDownClass(self):
        self.__fileSystem.close()

    def test_matchMultiple(self):
        for i, test in enumerate(input_output_pairs):
            print(f'ObjC Testing: {input_output_pairs_desc[i]}')
            path = f"member_property_{i}.h"

            self.__fileSystem.create(path, wipe=True)
            file = self.__fileSystem.open(path, mode="w")
            file.write(test[0])
            file.flush()
            file.close()
            self.__apiTagger.process(path)

            expectedContent = test[1]
            processedContent = self.__fileSystem.readtext(path)
            self.assertEqual(processedContent, expectedContent)

if __name__ == '__main__':
    unittest.main()
