package com.psrom.registration.service;

import com.psrom.registration.DTO.MemberDTO;
import com.psrom.registration.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class MemberService {
    private final MemberRepository memberRepository;

    public int save(MemberDTO memberDTO) {
        return memberRepository.save(memberDTO);
    }
}
